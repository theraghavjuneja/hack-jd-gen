from fastapi import FastAPI,HTTPException
import os
import uvicorn
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain.schema import StrOutputParser
import google.generativeai as genai
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
from helper_function import to_markdown
from fastapi.middleware.cors import CORSMiddleware
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
app=FastAPI(
    title="Gemini and Langchain Application",
    version="1.0",
    description="A simple API which provide 3 end-points each for description,summary and expansion"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",temperature=0.9,top_p=0.85)
summary_prompt_template=ChatPromptTemplate.from_template("""
    You are organizing a hackathon whose details are given below:
    {description}

    Your aim is to provide a detailed summary. Make sure to include the headers given below:
    - Hackathon name
    - Tagline (if provided, else generate one)
    - A brief overview
    - Objectives (if provided, else create them)
    - Eligibility criteria (if provided, else create them)
    - Prizes (if provided, else write 'This hackathon offers exciting prizes for the winners')
    - Phases and Timeline (if provided)
    - Who should participate(For example, if it is a blockchain based hackathon, You can write Participation is open to all, But those who are interested in blockchain based hackathon and know blockchain must participate)
    You are free to make more subheaders according to the input provided
    
    Additionally, ensure the generated content is SEO-friendly.                                                  
""")
detailed_prompt_template=ChatPromptTemplate.from_template("""
You are organizing a hackathon whose details are given below
    {description}


    Please provide a comprehensive and detailed description of the hackathon . Make sure to include the headers given below:
    - Hackathon name
    - Tagline (if provided, else generate one)
    - A brief overview
    - Objectives (if provided, else create them)
    - Eligibility criteria (if provided, else create them)
    - Prizes (if provided, else write 'This hackathon offers exciting prizes for the winners')
    - Phases and Timeline (if provided)
    - Who should participate(For example, if it is a blockchain based hackathon, You can write Participation is open to all, But those who are interested in blockchain based hackathon and know blockchain must participate)
    You are free to make more subheaders according to the input provided
    
    Additionally, ensure the generated content is SEO-friendly.
""")
detailed_job_template=ChatPromptTemplate.from_template("""
You are listing out your job on a platform.The details of jobs are given below
    {details}.
    
    Please provide a much comprehensive and a detailed job description. Make sure to include the headers given below
    -Designation of the Job
    -Years of Experience Required
    -Salary Offered
    -Vacancies
    -A Brief Overview of the Role(if not provided, think about the designation of the job and  generate a overview)
    -Detailed Roles and Responsibilities(if not provided, think about the roles and responsibilities of this designation. For example,A frontend engineer can have following role. Collaborating with design and backend teams to generate user-friendly and  responsive interfaces  )
    -Must-Have Skills(if not provided, think about skills of that job designation)
    -Secondary Skills
    -Benefits and Perks (if provided else think about Benfits a job role can have)
    -Location (if provided, else write 'Location details will be shared with selected candidates')
    -Certification Required (if provided, else say 'Certificates related to the {job designation} field are highly appreciated
    
    You are free to make more subheaders according to the input provided
    
    Additionally, ensure the generated content is SEO-friendly.   
""")


output_parser=StrOutputParser()

add_routes(app, llm, path="/gemini")
add_routes(app,summary_prompt_template|llm|output_parser,path='/summary')
add_routes(app,detailed_prompt_template|llm|output_parser,path="/details")
add_routes(app,detailed_job_template|llm|output_parser,path='/jobDescription')


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)