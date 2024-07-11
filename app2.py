from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
from fastapi.middleware.cors import CORSMiddleware

# Set all CORS enabled origins

app= FastAPI(title="Server", version="1.0", 
              description="A simple API Server")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.3)
add_routes(app, model, path="/gemini")
brief_prompt = ChatPromptTemplate.from_template("write a brief on the {topic}")
add_routes(app, brief_prompt | model, path="/brief")

funny_prompt = ChatPromptTemplate.from_template("Tell me something funny about {topic}")
add_routes(app, funny_prompt | model, path="/funny")
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000, reload=True)