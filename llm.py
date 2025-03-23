
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = "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"
)

response = llm.invoke("whats your mothers name")
print(response)