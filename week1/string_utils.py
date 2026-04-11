def count_vowels(text: str) -> int:
    """Returns the count of vowel characters (case-insensitive)."""
    if text is None: raise TypeError("Input cannot be None")
    return sum(1 for char in text.lower() if char in 'aeiou')

def reverse_string(text: str) -> str:
    """Returns the string with all characters in reversed order."""
    if text is None: raise TypeError("Input cannot be None")
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """Returns True if text reads same forwards and backwards (ignoring spaces/case)."""
    if text is None: raise TypeError("Input cannot be None")
    clean_text = "".join(text.lower().split())
    return clean_text == clean_text[::-1]

def word_count(text: str) -> int:
    """Returns the number of words in text separated by whitespace."""
    if text is None: raise TypeError("Input cannot be None")
    return len(text.split())

def capitalise_words(text: str) -> str:
    """Capitalises first letter of each word and the rest lowercase."""
    if text is None: raise TypeError("Input cannot be None")
    return " ".join(word.capitalize() for word in text.split())

def remove_duplicates(text: str) -> str:
    """Returns text with consecutive duplicate characters removed."""
    if text is None: raise TypeError("Input cannot be None")
    if not text: return ""
    result = [text[0]]
    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            result.append(text[i])
    return "".join(result)