# Ask how many students, then read each score in a for loop. Print the total, the average (2 decimals), and the highest score.

num_students = int(input("Students: "))

total = 0
highest = None

for i in range(1, num_students + 1):
  score = int(input(f"Score {i}: "))
  total += score

  if highest is None or score > highest:
    highest = score

average = total / num_students

print(f"Total: {total}   Avg: {average:.2f}")
print(f"Highest: {highest}")
