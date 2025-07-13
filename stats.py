def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(d):
    return d["num"]

def sort_char_count(char_dict):
    sorted_char_list = []
    for char in char_dict:
        sorted_char_list.append({"char" : char, "num" : char_dict[char]})
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list