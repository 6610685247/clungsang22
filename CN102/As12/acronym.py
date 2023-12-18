input_sentence = input().split(" ")

exception_word = ["a", "an", "at", "for", "i", "in", "of", "on", "the", "to", "with"]

new = ""

if input_sentence[0] in exception_word:
    new += input_sentence[0][0].upper()
else:
    new += input_sentence[0][0].upper()

for word in input_sentence[1:]:
    if word in exception_word:
        continue
    else:
        first_letter = word[0].upper()
        new += first_letter

print(f"{new}")
