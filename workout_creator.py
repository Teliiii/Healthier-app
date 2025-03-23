from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = ""
)

print("(this is going to be buttons) Enter your type of training, strength, cardio, muscle building, or flexibility")
training_type = input("")
print("Enter some muscle groups you want to prioritize:")
muscle_groups = input("")
print("Enter your workout time for the day in hours:")
workout_time = input("")
user_input = "Can you give me a workout that is based on "+training_type+" that focuses working out "+muscle_groups+", and is done within a strict time of "+workout_time+" hours. Only list the excercises numerically and a brief description on how to do them for each, along with their time/steps interval."
question = str(llm.invoke(user_input))
start_index = 9
end_index = question.find(' additional_kwargs=', start_index)
response = question[start_index:end_index-1]
final_response = "Here is your workout:\n"+response.replace(r'\n', '\n')
print(final_response)