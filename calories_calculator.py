from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = "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"
)

print("Enter your current height in inches")
current_height = input("")
print("Enter your current weight:")
current_weight = input("")
print("Enter your goal weight: ")
goal_weight = input("")
print("Enter the time frame you want to complete this weight loss in months")
time_period = input("")

user_input = "Can you tell me the direct range of the calories I should be consuming if I weigh "+current_weight+" pounds and I have a height of "+current_height+"inches, and I want to reach "+goal_weight+" pounds in "+time_period+" months? Only send the calories I should be consuming, no other information."
question = str(llm.invoke(user_input))
start_index = 9
end_index = question.find(' additional_kwargs=', start_index)
response = question[start_index:end_index-1]
response1 = response.replace(r'\n', '\n')
final_response = "You should be consuming "+response1.lower()
print(final_response)