def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        text = f.read()
    
    total_words = wordcount(text)
    char_dict = character_count(text)
    char_list = convert_to_list(char_dict)

    return total_words, char_list

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

def sort_on(dict):
    return dict["count"]

def convert_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

word_count_result, char_list_result = main()
print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count_result} words found in the document")
for char_dict in char_list_result:
    print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
print("---End Report---")