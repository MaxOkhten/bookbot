def get_num_words(text):

    return len(text.split())

def sort_on(items):
    return items["num"]

def sorted_list(char_count):
        chars_list = []
        for char, count in char_count.items():
            chars_list.append({"char": f"{char}", "num": count})

        chars_list.sort(reverse=True, key=sort_on)
        
        return chars_list

def character_counter(text):
    char_count = {}

    for element in text:
        
        if element.lower() in char_count:
            char_count[element.lower()] += 1
        
        else: 
            char_count[element.lower()] = 1

    return char_count

