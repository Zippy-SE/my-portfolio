#simpler code block:
#def calculate_age(birth_year):
#    current_year = 2023
#    age = current_year - birth_year
#    return age

#print(calculate_age(2000))

#alternate code block
def calculate_age(birth_year):
    current_year = 2025
    if birth_year > current_year:
        return "Invalid birth year"
    else:
        age = current_year - birth_year
        return age

user_birth_year = int(input("Enter your birth year: "))
print("You are", calculate_age(user_birth_year), "years old.")

