from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
load_dotenv()
_prompt = ChatPromptTemplate.from_template(
    "Tell me a joke about Chuck Norris and {text}")
_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",google_api_key=GOOGLE_API_KEY)

chain = _prompt | _model

chain.invoke({"text": "Cannelloni"})
# Here's a joke about Chuck Norris and Cannelloni:
# Chuck Norris doesn't eat cannelloni. He eats the can."