from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    
)

response = llm.invoke("whats your mothers name")
print(response)