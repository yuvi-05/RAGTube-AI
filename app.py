from flask import Flask,render_template,request,jsonify
import json

import requests
import joblib
import numpy as np
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query_embedding",methods=["POST"])
def embed():
    data= request.get_json()
    query = data["query"]

    def create_embeddings(text_list):
        r = requests.post("http://localhost:11434/api/embed",json={      # ollama api key : local instance of ollama runs on 11434 port 
          "model":"bge-m3",                                              # select model to create embeddings
          "input":text_list                                              # string to create embedding of
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

    que_embedding = create_embeddings([query])[0]

    similarity = cosine_similarity(np.vstack(df["embedding"]),[que_embedding]).flatten()

    top_result = 3

    max_index = similarity.argsort()[::-1][0:top_result]
    new_df = df.loc[max_index]
    # print(new_df[["video_name","start","text"]])
    print("Generating your answer...")

    prompt =f''' here are some chunks of vidoes lectures of engineering, with lecture_name, start_time(in seconds) and text :
    {new_df[["video_name","start","text"]]}
    ------------------------------------------------------------
    users question : {query}
    find related chunks text which matches best with answer of this question and summarize it , 
    provide response in json string format and dont mention anything about chunks :- 
    "user_query":{query}, 
    "summary"(2-3 paragraph):"summary", 
    "video_name" : "video name", 
    "timestamp" : "...seconds", 
    dont provide any other information or mention anything about chunk,
    '''

    initial_response = inference(prompt)
    dict_response = json.loads(initial_response)

    
    for i,time in enumerate(new_df["start"]):
        if time == dict_response.get("timestamp") :
            dict_response["video_name"] = new_df["video_name"].iloc[i]
            # attach video link (if available) and include start timestamp
            if "link" in new_df.columns:
                link = new_df["link"].iloc[i]
                if link:
                    ts = str(dict_response.get("timestamp", ""))
                    if ts:
                        if "?" in link:
                            link_with_ts = f"{link}&t={ts}"
                        else:
                            link_with_ts = f"{link}?t={ts}"
                    else:
                        link_with_ts = link
                    dict_response["video_link"] = link_with_ts
    
    # with open ("json_response.json","w") as f:
    #     json.dump(dict_response,f,indent=4)
    #     response=f


    # prompt_2 = f''' create json string ready to dump into variable from following string in format : 
    # "user_query":"(user query)"
    # "summary":"(summary)",
    # "video_name":"(video name)"
    # "timestamp":"(time stamp)"
    # --------------------------------------------------------------
    # string = {initial_response}
    # '''
    # response = inference(prompt_2)
    # if no specific matched link found, fall back to first available link
    if "video_link" not in dict_response and "link" in new_df.columns and len(new_df) > 0:
        first_link = new_df["link"].iloc[0]
        if first_link:
            ts = str(dict_response.get("timestamp", ""))
            if ts:
                if "?" in first_link:
                    dict_response["video_link"] = f"{first_link}&t={ts}"
                else:
                    dict_response["video_link"] = f"{first_link}?t={ts}"
            else:
                dict_response["video_link"] = first_link

    print((dict_response))
    print(new_df)
    
    return jsonify(dict_response)

app.run(debug=True)