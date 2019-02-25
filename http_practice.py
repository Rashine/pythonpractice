import requests, random
url = 'https://icanhazdadjoke.com/search'
user_input = ""
while True:
    user_input = input("Let me tell you a joke! Give me a topic: ")
    if user_input == 'QuitDadJokes':
        break
    res = requests.get(
        url,
        headers= {"Accept": "application/json"},
        params= {"term": user_input})
    if res.ok:
        data = res.json()
        if data["total_jokes"] >= 1:
            print(data["results"][random.randint(0,data["total_jokes"])]["joke"]+"\n")
        else:
            print(f"There is no joke about {user_input}, sorry.\n")
        print("To quit using the key string 'QuitDadJokes'")
    else:
        print("you get a wrong request.")