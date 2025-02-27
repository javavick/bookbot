def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}

    for char in text:
        lowercase_char = char.lower()
        char_count[lowercase_char] = 1 if lowercase_char not in char_count else char_count[lowercase_char] + 1

    return char_count

def sort_char_count(char_count):
    char_list = []

    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(key=lambda dict: dict["count"], reverse=True)

    return char_list 
