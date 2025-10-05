import os,subprocess

os.makedirs("audios",exist_ok=True)
files = (os.listdir("videos"))

for file in files:
    if file.endswith(".mp4"):
      subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{file}.mp3"])   # subprocess.run -> runs command on terminal , ffmpeg -> tools to deal with audio and video , -i -> flag next file is input file
      print(f"{file} converted to mp3 successfully!")