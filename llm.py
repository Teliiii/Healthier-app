from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = "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"
)

response = llm.invoke("Hello, how are you?")
print(response)