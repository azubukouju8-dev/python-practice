# Exercise 1: Variables and data types
# Shows the main built-in data types in Python.

name = "Uju"                    # str (text)
age = 21                        # int (whole number)
height_m = 1.68                 # float (decimal number)
is_learner = True               # bool (True or False)
skills = ["AI automation", "Python", "n8n", "ElevenLabs", "MySQL", "Supabase", "API integration", "JavaScript"]  # list (a collection of items)

print(f"Name: {name} -> {type(name).__name__}")
print(f"Age: {age} -> {type(age).__name__}")
print(f"Height: {height_m} -> {type(height_m).__name__}")
print(f"Learner: {is_learner} -> {type(is_learner).__name__}")
print(f"Skills: {skills} -> {type(skills).__name__}")

# Type conversion: turning one type into another
age_text = str(age)
print("Age as text:", age_text + " years old")