import string

sentence = input("Input a sentence: ")

sentences = sentence.split(".")
unique_letters = []

for sentence in sentences:
    for letter in sentence:
        if letter not in unique_letters and letter.isalpha():
            unique_letters.append(letter)

# Here you should add the missing part

print("Unique letters:", unique_letters)
