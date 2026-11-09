# Read a sentence. Loop over every character and count the vowels (upper- and lowercase). Print the count.

sentence = input("Sentence: ")

vowels = "aeiouAEIOU"
count = 0

for char in sentence:
  if char in vowels:
    count += 1

print(f"Vowels: {count}")
