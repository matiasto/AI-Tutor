#####################################
## BASIC SCRIPT MAM01 AI ASSISTANT ##
## Made by Charlotte Lafage        ##
## Last update: 09-09-2024         ##
## For Amsterdam UMC - KIK         ##
#####################################

import requests

api_endpoint = "https://uva-ai-dbeqd9hbh9hjcxgk.swedencentral-01.azurewebsites.net/chat/completions"

######## TO FILL BY STUDENT #########
student_ai_name = "your AI"
student_api_key = "" #: Set your own API key here
student_llm = "gpt-4" # Can be gpt-35-turbo, gpt-4-turbo, gpt-4 or Meta-Llama-3-8B-Instruct.
student_initial_prompt = "You are an assistant and students are going to ask you questions. You initiate the following conversation by asking the student what help they need."
#####################################


####### API REQUEST FORMATTING ######
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + student_api_key
}

data = {
    "model": student_llm,
    "messages": [],
}
######################################

####### MAIN FUNCTIONS ###############
def get_ai_answer(user_input):
    """Sends an API request to the UvA AI chatbot using the globally declared request data and updating it with user_input.

    Args:
        user_input (string): user request to the chatbot

    Returns:
        string: the chatbot's answer, taken from the API request response
    """
    data["messages"].append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(url=api_endpoint, headers=headers, json=data)

    if response.status_code == 200:
        data_response = response.json()
        return(f'\n<<{student_ai_name}>> {data_response["choices"][0]["message"]["content"]}')
    else:
        print(f"Failed to connect to API. Status code: {response.status_code}")
        print(response.text)
        return ""

####### MAIN LOOP ####################
print(f"Loading {student_ai_name} ...")
get_ai_answer(student_initial_prompt) # This gives the chatbot the initial prompt

user_input = input("[Type 'stop' to stop the conversation]\n<<You>> ")

while (user_input != "stop"):
    print(get_ai_answer(user_input))
    user_input = input("\n<<You>> ")