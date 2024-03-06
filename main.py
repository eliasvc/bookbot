def sort_on(dict):
    """Sorting function for a dictionary using key 'num'"""
    return dict["num"]

def count_words(text):
    """Return the amount of words in a text"""
    return len(text.split())

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
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        
        print(f"--- Begin report of {book_path} ---")
        print(f"{count_words(file_contents)} words found in document\n\n")

        # Only interested in the letters of the alphabet
        alpha_only = [{"char": char, "num": num} for char, num in count_letters(file_contents).items() if char.isalpha()]
        alpha_only.sort(reverse=True, key=sort_on)
        for letter in alpha_only:
            print(f"The {letter['char']} character was found {letter['num']} times")
        print ("--- End report---")

if __name__ == "__main__":
    main()