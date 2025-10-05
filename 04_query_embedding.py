import requests
import joblib
import numpy as np
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={      # ollama api key : local instance of ollama runs on 11434 port 
        "model":"bge-m3",                                            # select model to create embeddings
        "input":text_list                                            # string to create embedding of
    })

    return r.json()["embeddings"]

def inference (prompt):
    r = requests.post("http://localhost:11434/api/generate",json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream" : False
    })

    return r.json()["response"]

df=joblib.load("embeddings.joblib")

que = input("Ask me a question..")
que_embedding = create_embeddings([que])[0]

similarity = cosine_similarity(np.vstack(df["embedding"]),[que_embedding]).flatten()

top_result = 3

max_index = similarity.argsort()[::-1][0:top_result]
new_df = df.loc[max_index]
# print(new_df[["video_name","start","text"]])
print("Generating your answer...")

prompt =f''' here are some chunks of vidoes lectures of engineering, with lecture_name, start_time(in seconds) and text :
{new_df[["video_name","start","text"]]}
------------------------------------------------------------
users question : {que}
find related chunks text which gives best answer to this question and summarize it , 
provide response in this paragraph format :- 
1.user question:..., 
2.summary(2-3 paragraph):..., 
3.video name = ..., 
4.timestamp = ..., 
dont provide any other information or mention anything about chunk,
'''

response = inference(prompt)
print (response,f" {new_df[['video_name']]}")