# Name: Fadel Muhammad Naufal
# NIM: 2611533017
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])


text = "Fadel Muhammad Naufal"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)