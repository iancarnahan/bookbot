def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    total_words = wordcount(file_contents)
    return total_words

def wordcount(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

word_count_result = main()
print(word_count_result)

main()