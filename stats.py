def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def get_word_count(filepath):
    text = get_book_text(filepath)
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def get_character_count(filepath):
    character_dictionary = {}
    dictionary_list = []
    text = get_book_text(filepath)
    lower_text = text.lower()
    for character in lower_text:
        if character.isalpha():
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1

    for key, count in character_dictionary.items():
        single_character_dictionary = {"char":key, "num":count}
        dictionary_list.append(single_character_dictionary)
    return sorted(dictionary_list, key=lambda d: d['num'], reverse=True)
