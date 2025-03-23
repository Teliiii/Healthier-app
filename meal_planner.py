from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = ""
)

print("Enter your daily calorie budget here:")
calorie_budget = input("")
print("List any ingredients you have available or that you prefer:")
preferred_foods = input("")
print("List any dietary restrictions you have here (type \"none\" if you dont have any):")
prohibited_foods = input("")
user_input = ""
if prohibited_foods == "none":
    user_input = "Give me a recipe for a quick, healthy, and protein filled meal that fits well within my "+calorie_budget+" calorie budget, and can you make sure to include "+preferred_foods+" in the recipe. Can your output only the title of the dish on the top, include a list of ingredients right after the title, and the procedures numerically labled at the bottom."
else:
    user_input = "Give me a recipe for a quick, healthy, and protein filled meal that fits well within my "+calorie_budget+" calorie budget, and can you make sure to include "+preferred_foods+" in the recipe, and keep in mind that I specifically can't eat "+prohibited_foods+" due to dietary restrictions. Can your output only the title of the dish on the top, include a list of ingredients right after the title, and the procedures numerically labled at the bottom."
question = str(llm.invoke(user_input))
start_index = 9
end_index = question.find(' additional_kwargs=', start_index)
response = question[start_index:end_index-1]
final_response = response.replace(r'\n', '\n')
print(final_response)