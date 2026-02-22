# Count Words
def count_words(text):
    return len(text.split())
# Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
# Count Consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)
# Reverse Text
def reverse_text(text):
    return text[::-1]
# Check Palindrome
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
# Remove Vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)
# Word Frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
# Longest Word
def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest
# Analyze Text
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    longest = longest_word(text)
    print(f"Longest word: {longest} ({len(longest)} letters)")
    freq = word_frequency(text)
    print("Word Frequency:", end=" ")
    print(", ".join(f"{k}: {v}" for k, v in freq.items()))

# Main
text = input("Enter text: ")
analyze_text(text)