weather = input("How's the weather today? (sunny, rainy, cloudy): ").lower()
if weather == "sunny":
    print("How about going for a walk!?")
elif weather == "rainy":
    print("Stay in and read a book!")
elif weather == "cloudy":
    print("Would you like a side of meatballs with that?")
else:
    "Please enter a valid choice."