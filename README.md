# 🎥 RAGTube AI

**RAGTube AI** is an intelligent **Retrieval-Augmented Generation (RAG)** system that answers user queries based on your dataset.  
It not only summarizes the information but also provides **relevant YouTube video links with exact timestamps** to help users visualize the concept instantly.
*NOTE : This AI is trained on limited dataset so it may provide incorrect response *

---

## 🚀 Features

✅ Query any topic related to your dataset  
✅ Summarized AI responses  
✅ YouTube video link with **exact timestamp**  
✅ Embedding-based semantic search  
✅ Simple and elegant Flask web interface  

---

## ⚙️ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/ragtube-ai.git
   cd ragtube-ai
   
2. Install dependencies 
   *NOTE : Downlaod and install ollama and pull bge-m3 and llama3.2 model to use it on your localhost, else you cannot use it*
   pip install -r requirements.txt
   
4. Run the Flask app
   python app.py

5. Open your browser and go to
   👉 http://127.0.0.1:5000

🧠 How It Works

1.The user submits a query through the web interface.

2.The query is converted into an embedding using a model ( BGE-M3).

3.Cosine similarity is computed against pre-stored document embeddings.

4.The top results are passed to an LLM for summarization.

5.The system returns:
 - A concise summary
 - A YouTube video link with an exact timestamp

📄 License
This project is licensed under the MIT License.

👤 Author
Yuvraj Dake
📧 yuvrajdake9105@gmail.com


