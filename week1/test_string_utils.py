import pytest
from string_utils import *

# --- count_vowels tests ---
def test_count_vowels_standard(): assert count_vowels("Hello") == 2
def test_count_vowels_empty(): assert count_vowels("") == 0
def test_count_vowels_none_raises_typeerror():
    with pytest.raises(TypeError): count_vowels(None)

# --- reverse_string tests ---
def test_reverse_string_standard(): assert reverse_string("abc") == "cba"
def test_reverse_string_single_char(): assert reverse_string("a") == "a"
def test_reverse_string_none_raises_typeerror():
    with pytest.raises(TypeError): reverse_string(None)

# --- is_palindrome tests ---
def test_is_palindrome_standard(): assert is_palindrome("racecar") is True
def test_is_palindrome_complex(): assert is_palindrome("A man a plan a canal Panama") is True
def test_is_palindrome_none_raises_typeerror():
    with pytest.raises(TypeError): is_palindrome(None)

# --- word_count tests ---
def test_word_count_standard(): assert word_count("Hello World") == 2
def test_word_count_spaces(): assert word_count("  spaces  ") == 1
def test_word_count_none_raises_typeerror():
    with pytest.raises(TypeError): word_count(None)

# --- capitalise_words tests ---
def test_capitalise_words_standard(): assert capitalise_words("hello world") == "Hello World"
def test_capitalise_words_mixed(): assert capitalise_words("sQE lAB") == "Sqe Lab"
def test_capitalise_words_none_raises_typeerror():
    with pytest.raises(TypeError): capitalise_words(None)

# --- remove_duplicates tests ---
def test_remove_duplicates_standard(): assert remove_duplicates("aaabbbcc") == "abc"
def test_remove_duplicates_long_seq(): assert remove_duplicates("aaaaa") == "a"
def test_remove_duplicates_none_raises_typeerror():
    with pytest.raises(TypeError): remove_duplicates(None)