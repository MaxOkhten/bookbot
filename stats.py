def get_num_words(text):

    return len(text.split())

def character_counter(text):
    char_count = {}

    for element in text:
        
        if element.lower() in char_count:
            char_count[element.lower()] += 1
        
        else: 
            char_count[element.lower()] = 1

    return char_count

