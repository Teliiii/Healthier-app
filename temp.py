from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = ""
)
print("Ask me anything! Press Q to quit.")
while True:
    user_input = input("")
    if user_input == 'Q':
        break
    question = str(llm.invoke(user_input))
    start_index = 9
    end_index = question.find(' additional_kwargs=', start_index)
    response = question[start_index:end_index-1]
    print(response)