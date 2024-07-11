from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from langserve import RemoteRunnable

funny_chain= RemoteRunnable("http://localhost:8000/funny/")

funny_chain.invoke({"topic": "parrots"})