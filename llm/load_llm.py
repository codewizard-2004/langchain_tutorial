# This module will be used to load the llm
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
google_key = os.environ.get("GOOGLE_API_KEY")

# initializing the LLM

def initialize_llm(temp: float = 0.5) -> ChatGoogleGenerativeAI:
    llm = ChatGoogleGenerativeAI(
        model = "gemini-1.5-flash",
        api_key = google_key,
        temperature = temp
    )
    print("LLM ready:", type(llm).__name__)

    return llm