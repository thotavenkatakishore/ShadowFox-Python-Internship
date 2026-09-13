total_jacks = 0

for i in range(10):

    # Complete 10 jumping jacks
    total_jacks += 10

    print("You completed 10 jumping jacks.")
    print("Total jumping jacks:", total_jacks)

    # Check if workout is complete
    if total_jacks == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? ")

    if tired.lower() == "yes" or tired.lower() == "y":

        skip = input("Do you want to skip the remaining sets? ")

        if skip.lower() == "yes" or skip.lower() == "y":
            print("You completed a total of", total_jacks, "jumping jacks.")
            break

        else:
            remaining = 100 - total_jacks
            print("You have", remaining, "jumping jacks remaining.")

    else:
        remaining = 100 - total_jacks
        print("You have", remaining, "jumping jacks remaining.")
        