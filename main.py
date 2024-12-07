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
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

word_count_result, char_count_result = main()
print(word_count_result)
print(char_count_result)