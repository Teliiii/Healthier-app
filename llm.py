from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    api_key = "sk-ycFpnouWkNuSL_wlXEAV0nOotkyq93vd3TU6TUCD_fT3BlbkFJfMWzsbh13DnU3MDVjws7psbq_Gug0Ovx5e5TtUDCAA"
)

response = llm.invoke("Hello, how are you?")
print(response)