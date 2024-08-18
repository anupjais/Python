weather = input("Enter weather condition : ").lower()

activity = "Go for a walk" if weather == "sunny" else "Read a book" if weather == "Rainy" else "Build a \"Snowman\"" if weather=="snowy" else "Korean Serise dekhana band karo"

print(activity)