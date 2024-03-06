def count_words(text):
    """Return the amount of words in a text"""
    return len(text)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

if __name__ == "__main__":
    main()