# Taking input from user
sentence = input("Enter a sentence: ")

print("Original:", sentence)

print("Characters (with spaces):", len(sentence)) # Characters count (with spaces)

no_spaces = sentence.replace(" ", "")
print("Characters (without spaces):", len(no_spaces)) # Characters count (without spaces)

words = sentence.split()
print("Words:", len(words)) #word count

print("UPPERCASE:", sentence.upper()) #uppercase

print("lowercase:", sentence.lower()) #lowercase

print("Title Case:", sentence.title()) #title case

if len(words) > 0:
    print("First word:", words[0]) #first word
    print("Last word:", words[-1]) #last word

print("Reversed:", sentence[::-1]) #reversed