def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        word_number = len(word_list)
        letter_tracker = {}
        word_count = f"{word_number}"
        file_contents_lower = file_contents.lower().split()
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        # print(alphabet)
        for words in file_contents_lower:
            for letters in words:
                if letters in alphabet and letters in letter_tracker:
                    letter_tracker[letters] += 1
                elif letters in alphabet:
                    letter_tracker[letters] = 1

        print(letter_tracker)
        print(word_count)


main()
