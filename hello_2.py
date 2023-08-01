first_name =  input("What is your first name? ")

print("Hello,", first_name)

if first_name == "Emmanuel":
    print(first_name, "is learning Python")
elif first_name == "Maximiliane":
    print(f"{first_name}, is learning with fellow students in the community!")
else:
    age  = int(input("How old are you? "))
    if age <= 6:
        print(f"Wow you're {age}! If you're confident with your reading already...")
    print(f"You should totally learn Python, {first_name}!")
print(f"Have a great day {first_name}!")

