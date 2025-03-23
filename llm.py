from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = "sk-ycFpnouWkNuSL_wlXEAV0nOotkyq93vd3TU6TUCD_fT3BlbkFJfMWzsbh13DnU3MDVjws7psbq_Gug0Ovx5e5TtUDCAA"
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