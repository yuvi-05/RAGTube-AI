import requests
import json
import pandas as pd
import os
import joblib
import time
start = time.time()


def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={      # ollama api key : local instance of ollama runs on 11434 port 
        "model":"bge-m3",                                            # select model to create embeddings
        "input":text_list                                            # string to create embedding of
    })

    return r.json()["embeddings"]


# Grouping 5 chunks to 1 :
os.makedirs("json2",exist_ok=True)
files = os.listdir("json")


for file in files:
    with open (f"json/{file}","r") as f:
        data = json.load(f)

    new_chunks=[]
    chunks = data["chunks"]
    text=""   
    start=""
    video_name=""


    for i,chunk in enumerate(chunks):
        
        if i%5==0:
            start =chunk["start"]
            text=""

        video_name = chunk["vid_name"]
        text+=chunk["text"] + " "

        if (i%5==4) or (i==len(chunks)-1):
            new_chunks.append({"start":start,"video_name":video_name,"text":text.strip()})
          

    print(f"for video : {file}")
    print(f"before chunks: {len(data['chunks'])} after chunks : {len(new_chunks)}")        
            
    with open(f"json2/{file}","w") as f:
        json.dump({"chunks":new_chunks},f,indent=4)       
         
# Embedding to vectors
files2 = os.listdir("json2")
dataframe = []

for file in files2:
    print(f"opening {file}")

    with open (f"json2/{file}") as f:
        json_file = json.load(f)
    # print(type(json_file))    

    print(f"embedding {file}")    
    # embedding = create_embeddings([c["text"] for c in json_file["chunks"]])
    # print(embedding) 
    # break    

    embeddings = create_embeddings([c["text"] for c in json_file["chunks"]])

    for i,chunk in enumerate(json_file["chunks"]):
        chunk["embedding"] = embeddings[i]
        dataframe.append(chunk)

# Saving to joblib file
df = pd.DataFrame.from_records(dataframe)
joblib.dump(df,"embeddings.joblib")

end= time.time()
print(f"time requird : {end-start} seconds")