from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
