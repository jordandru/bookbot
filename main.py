import sys
from stats import count_words, count_chars, sort_chars_by_count

def main():
    if len(sys.argv) < 2:
        # Not enough arguments were provided
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status code 1 to indicate an error
    
    path = sys.argv[1]
    
    text = ""
    with open(path, "r") as f:
        text = f.read()
    
    word_count = count_words(text)
    char_counts = count_chars(text)
    sorted_chars = sort_chars_by_count(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character count
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
