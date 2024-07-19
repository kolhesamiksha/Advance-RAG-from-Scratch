# Advance-RAG-from-Scratch- Chatbot 

An AI Assistant to help you solve Any Queries Regarding NVIDIA's CUDA Framework

## About

This Application is able

![advance-rag-workflow](https://github.com/user-attachments/assets/f66d9c12-5356-4b48-8a2e-1a4551181f57)

## Approach: RAG Workflow Stratergy

The approaches Followed for building RAG pipeline is discussed below

1. **WebCrawling**: 

2. **Semantic Chunking Techniques**:

3. **Metadata Chunking Method**:

3. **Embedding Models**:

4. **Vector-Store**:

5. **Query-Compression Techniques: Self-Query retrieval for metadata & MultiQuery**

6. **Hybrid-search**:

7. **Reranking Techniques**:

8. **LLM Model**:


## Results

**Features**: In the Results Along with Response you get, Latency(time require to process the Request) ,Cost-per-request, Query evaluation metrices

## Code Structure

```
    Chatbot-streamlit/
        ├── css/
        │ └── style.css
        ├── src/
        │ ├── logs/
        │ ├── utils/
        │ │ ├── init.py
        │ │ ├── custom_utils.py
        │ │ ├── get_insert_mongo_data.py
        │ │ ├── logutils.py
        │ │ └── mongo_init.py
        │ ├── api.py
        │ ├── main.py
        │ ├── schema.py
        │ └── test.py
        ├── ui/
        │ ├── sidebar.md
        │ └── styles.md
        ├── app.py
        ├── requirements.txt
        └── vercel.json
    images/
        ├── advance-rag-workflow.PNG
    Milvus_features_pipeline/
        ├── Milvus_Feature_Pipeline_Final.ipynb
    Research_Notebooks/
        ├── Milvus_Feature_Pipeline_sample.ipynb
    Retriever_Pipeline/
        ├── Retriever_Pipeline.ipynb
```

## TechStack

- Python
- MongoDB (Store API Secrets)
- Generative AI
- RAG Chatbot
- Langchain
- Web Scraping
- Semantic Router
- Ragas(RAG Evaluation)

## How to Run the Application

> Note: Code is builted and tested on python==^3.11.5

This Application is Not yet deployed.. In-progress.

Follow Below Instruction for smooth and Errorless Application Run
**Setup the Virtual-env**

    ```
    conda create --name ragapp python=3.11.5
    conda activate ragapp

    cd Chatbot-streamlit/
    pip install -r requirements.txt

**Setup the API Backend**

To Run the Application Locally First Run the FastAPI backend. Follow Below Instructions to Run the FastAPI:

**Note**: To add your credentials inside the Mongodb Atlas cloud to connect the application Refere: Chatbot-streamlit/src/utils/mongo_init.py

1. Run the API
    ```
    #Export Envs: After insderting daa into mongodb atlas cloud
    export CONNECTION_NAME=<chatbot-connection-name>

    #Now Run the FastAPI using below command and Relative Path as Chatbot-streamlit/
    uvicorn src.main:app --reload

    
Now /predict Endpoint of FastAPI is getting exposed, which can be used in out Streamlit app to do Q&A over RAG.

2. Check the API working in swagger

    ```
    Click on the link e.g http://127.0.0.1:8000/docs to check the swagger

**Setup the Streamlit UI**

To Run the Streamlit Application Locally Follow below Instructions to Run the App

    ```
    streamlit run app.py

This Will open a streamlit application where you can ask your questions and get the responses via API you exposed.

## Sample Output



**for more details**
Happy to Connect!! [Samiksha Kolhe](https://www.linkedin.com/in/samiksha-kolhe25701/)