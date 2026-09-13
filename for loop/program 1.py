import random

times_6 = 0
times_1 = 0
two_sixes = 0
previous_roll = 0

# Roll the die 20 times
for i in range(20):
    roll = random.randint(1, 6)

    print("Roll", i + 1, ":", roll)

    # Count 6s
    if roll == 6:
        times_6 += 1

    # Count 1s
    if roll == 1:
        times_1 += 1

    # Count two 6s in a row
    if roll == 6 and previous_roll == 6:
        two_sixes += 1

    previous_roll = roll

print("\nStatistics:")
print("How many times you rolled a 6:", times_6)
print("How many times you rolled a 1:", times_1)
print("How many times you rolled two 6s in a row:", two_sixes)