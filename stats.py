def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list
