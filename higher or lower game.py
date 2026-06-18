import random

print('''   _  _ _      _   _                       _                       _  
 | || (_)__ _| |_| |_ ___ _ _   ___ _ _  | |   _____ __ _____ _ _| | 
 | __ | / _` | ' |  _/ -_| '_| / _ | '_| | |__/ _ \ V  V / -_| '_|_| 
 |_||_|_\__, |_||_\__\___|_|   \___|_|   |____\___/\_/\_/\___|_| (_) 
        |___/                                                         
       
    ''')
print("🔥WELCOME TO THE HIGHER OR LOWER GUESSING GAME!!🔥\n psst...lets hope u lose!!")
data = [
    {"name": "Cristiano Ronaldo", "follower_count": 630, "description": "Footballer", "country": "Portugal"},
    {"name": "Ariana Grande", "follower_count": 380, "description": "Musician and actress", "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": 395, "description": "Actor and professional wrestler", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": 400, "description": "Reality TV personality and businesswoman", "country": "United States"},
    {"name": "Lionel Messi", "follower_count": 490, "description": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "follower_count": 430, "description": "Musician and actress", "country": "United States"},
    {"name": "Taylor Swift", "follower_count": 415, "description": "Musician", "country": "United States"},
    {"name": "Neymar", "follower_count": 220, "description": "Footballer", "country": "Brazil"},
    {"name": "Virat Kohli", "follower_count": 270, "description": "Cricketer", "country": "India"},
    {"name": "Kim Kardashian", "follower_count": 360, "description": "Reality TV personality and businesswoman", "country": "United States"},
    {"name": "Billie Eilish", "follower_count": 110, "description": "Musician", "country": "United States"},
    {"name": "Zendaya", "follower_count": 190, "description": "Actress and singer", "country": "United States"},
    {"name": "Shakira", "follower_count": 90, "description": "Musician", "country": "Colombia"},
    {"name": "Kylian Mbappé", "follower_count": 120, "description": "Footballer", "country": "France"},
    {"name": "Emma Watson", "follower_count": 80, "description": "Actress", "country": "United Kingdom"},
    {"name": "NASA", "follower_count": 100, "description": "Space agency", "country": "United States"},
    {"name": "Narendra Modi", "follower_count": 90, "description": "Prime Minister", "country": "India"},
    {"name": "Elon Musk", "follower_count": 180, "description": "Entrepreneur", "country": "United States"},
    {"name": "MrBeast", "follower_count": 110, "description": "YouTuber", "country": "United States"},
    {"name": "Blackpink", "follower_count": 95, "description": "Musical group", "country": "South Korea"}
]
item1 = random.choice(data)
score = 0

while True:    
    item2 = random.choice(data)

    while item1==item2:
        item2 = random.choice(data)

    print(f"compare A: {item1['name']}, a {item1['description']}, from {item1['country']}.")
    print("\n\nVs\n\n")
    print(f"\n against B: {item2['name']}, a {item2['description']}, from {item2['country']}.")
    guess = input("who has more followers? type A or B:\n").lower()

    print("\n"*100)
    print('''   _  _ _      _   _                       _                       _  
 | || (_)__ _| |_| |_ ___ _ _   ___ _ _  | |   _____ __ _____ _ _| | 
 | __ | / _` | ' |  _/ -_| '_| / _ | '_| | |__/ _ \ V  V / -_| '_|_| 
 |_||_|_\__, |_||_\__\___|_|   \___|_|   |____\___/\_/\_/\___|_| (_) 
        |___/                                                         
       
    ''')
    if guess == "a":
        if item1["follower_count"] > item2["follower_count"]:
            score+=1
            print(f"you are right! \ncurrent score is:{score}")
        else:
            print(f"sorry! that is wrong.\nyour final score is:{score}")
            break
    elif guess == "b":
        if item1["follower_count"] < item2["follower_count"]:
            score+=1
            print(f"you are right! \ncurrent score is:{score}")
        else:
            print(f"sorry! that is wrong.\nyour final score is:{score}")
            break
    else:
        print("your guess is invalid.\n you freak! don't you have eyes?!\ntype A or B, i didn't ask your life history!\n oof! kids these day!\n\nSTART AGAIN!!\n")
    print(f"\n {item1['name']}, {item1['follower_count']}.\n {item2['name']}, {item2['follower_count']}.")
    item1=item2