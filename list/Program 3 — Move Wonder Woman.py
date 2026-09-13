# Create the Justice League list
justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

# Display the updated list
print("After moving Wonder Woman to the beginning:")
print(justice_league)