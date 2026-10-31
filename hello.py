name = input("What's your name? ")
goal = input("What job are you training for? ")
study = float(input("How many hours will you study this week? "))
per_day = round(study/6, 1)

print(f"Hi {name}! Day 1 of becoming {goal} starts now. I'll study {study} hours this week, about {per_day} hours a day.")
