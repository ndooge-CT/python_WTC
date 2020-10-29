
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """
    
    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    word_list = split(' ,.?;!', text)
    new_list = []
    for i in word_list:
        if len(i) > 0: 
            new_list.append(i.lower())
    return new_list

def words_longer_than(length, text):
    word_list = convert_to_word_list(text)
    new_list = []
    for i in word_list:
        if len(i) > length:
            new_list.append(i)
    return new_list


def words_lengths_map(text):
    word_list = convert_to_word_list(text)
    counts = {}
    for i in word_list:
        if len(i) not in counts:
            counts[len(i)] = 1
        else:
            counts[len(i)]+=1
    
    return counts

def get_alphabet_characters():
    return ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def letters_count_map(text):
    if text == None:
        return None
    from collections import Counter 
    letters = get_alphabet_characters()
    word_list = convert_to_word_list(text)
    word_str = ''.join(word_list)
    chars_in_string = Counter(word_str)
    
    res = {}
    for letter in letters:
        if(letter in chars_in_string):
            res[letter] = chars_in_string[letter]
        else: 
            res[letter] = 0 
    return(res)


def most_used_character(text):
    if text == None or text == '':
        return None
    letter_count = letters_count_map(text)
    #my_counter_dict = {}
    #for v in input_dict.values():
       # my_counter_dict[v] = my_counter_dict.get(v, 0)+1
    #>>> max(my_counter_dict.iterkeys(), key=my_counter_dict.get)
    most_used = max(letter_count.keys(),key=letter_count.get)
    return most_used