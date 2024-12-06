def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        text = f.read()
    total_words = wordcount(text)
    return total_words

def wordcount(text):
    words = text.split()
    return len(words)

word_count_result = main()
print(word_count_result)

main()