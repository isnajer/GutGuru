import openai
from keys import API_KEY

openai.api_key = API_KEY

messages = []
system_msg = "Welcome to GutGuru! I'm here to help you make informed dietary choices based on your symptoms or health conditions. \nPlease enter a health condition or describe your symptoms, and I will provide you with suggestions on foods to eat or avoid. \n\nIf you'd like to end our conversation, simply type 'quit'.\n"
messages.append({"role": "system", "content": system_msg})
print(system_msg + "\n")

default_prompt = "What are 3 foods I should eat and 3 foods I should avoid to prevent "
more_options_prompt = "Give me more options"

while True:
    user_input = input("")
    if user_input.lower() == "quit":
        break

    message = default_prompt + user_input
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print(reply + "\n")

    while True:
        follow_up = input(
            "Was this helpful? (yes/more options/new request): \n").lower()
        if follow_up == "yes":
            # print("Great! I hope you feel better!")
            break
        elif follow_up == "more options":
            messages.append({"role": "user", "content": more_options_prompt})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})

            print("\n" + reply + "\n")
        elif follow_up == "new request":
            break
        else:
            print(
                "Invalid input. Please type 'yes', 'more options', 'new request', or 'quit'. \n")

    if follow_up.lower() == "yes":
        print("Great! I hope you feel better!")
        break
    elif follow_up.lower() == "quit":
        break
