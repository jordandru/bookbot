def count_words(book):
    split_words = book.split()
    words = len(split_words)
    return words

def count_chars(book):
    lowercase_text = book.lower()
    
    char_counts = {}
    
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

# How we looking?

def sort_chars_by_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"character": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list