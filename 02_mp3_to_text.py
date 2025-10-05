import whisper,os,json,subprocess,time
start = time.time()
mp3_files = os.listdir("audios")

# Clean audio :
os.makedirs("cleaned_audio",exist_ok=True)
print("cleaning audio...")

for file in mp3_files:
    subprocess.run(["ffmpeg","-i",f"audios/{file}","-ac","1","-ar","16000",f"cleaned_audio/{file}.wav"])   # -ac,1 -> audio channel =1 , -ar,16000 -> audio sample rate = 16khz
    print(f"{file} cleaned!")

print("All audio files are cleaned !!")
print("Loading large-v2 model for transcribing..") 
wav_files = os.listdir("cleaned_audio")   

model = whisper.load_model("large-v2")

print("Model loaded sucessfully !!")
print("translating audio to text...")

os.makedirs("json",exist_ok=True)

for i,file in enumerate(wav_files):
    start1=time.time()

    if f"{file}.json" not in os.listdir("json"):

        print(f"{file} translation started")

        raw_text = model.transcribe(audio=f"cleaned_audio/{file}",   # transcribe method used to convert audio to text
                                language="hi", 
                                task="translate",             # translates foreign language to eng
                                temperature=0,
                                beam_size=1,         
                                word_timestamps=False)    # returns timestamp for each word 
        
        print(f"{file} translation complete! ")
        print(f"{i+1} videos completed , {100-i-1} videos remaining ...")
        
        chunk =[]  

        for segment in raw_text["segments"]:
            chunk.append({"vid_name":f"{file}","start":segment["start"],"text":segment["text"]})
        chunk_metadata={"chunks":chunk,"text":raw_text["text"]}    
        
        with open(f"json/{file}.json","w") as f:
            json.dump(chunk_metadata,f)
        end1 = time.time()    
        print(f"Time required for {file} is {(end1-start1)/60} minutes")

end = time.time()    
print(f"time required for all videos is {(end-start)/3600} hours")