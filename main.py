def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        text = f.read()
    
    total_words = wordcount(text)
    char_count = character_count(text)

    return total_words, char_count

def wordcount(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

word_count_result, char_count_result = main()
print(word_count_result)
print(char_count_result)