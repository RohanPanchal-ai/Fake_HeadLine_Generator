import random
subjects=[
    " shahrukh khan",
    " virat kohli",
    " Nirmala Sitharaman",
    " A mumbai cat",
    " prime minister modi",
    " auto rickshaw driver from delhi"
    ]
         
actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
    ]
place_or_things=[
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL matchs",
    "at india gate"
    ]
while True:
    subject = random.choice(subjects)
    action =  random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline =f"BREAKNG NEWS:{subject} {action} {place_or_thing}"
    print("\n"+headline)

    user_input=input("\n Do you want another headline?(yes/no):").strip().lower()
    if user_input == "no":
        break
   
print("\n thanks for using the fake news headline generator. have a fun day")
    
    
