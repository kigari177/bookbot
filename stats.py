def get_word_count(words):
    return len(words.split())    
def get_character_count(words):
    word_dictionary = {}
    for word in words:
        something = word.lower()
        if something in word_dictionary:
            word_dictionary[something] += 1
        else:
            word_dictionary[something] = 1
    return word_dictionary

def get_sorted_chars(some_dict):
    sorted_dict = sorted(some_dict.items(), key=lambda x:x[1], reverse=True)
    some_list = []
    for key,value in sorted_dict:
        if key.isalpha():
            some_list.append({key: value})
    return some_list
