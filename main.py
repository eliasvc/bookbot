def count_words(text):
    """Return the amount of words in a text"""
    return len(text)

def count_letters(text):
    """Return a dictionary with the count of each characters in a text"""
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1
    
    return char_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

        print(count_letters(file_contents))

if __name__ == "__main__":
    main()