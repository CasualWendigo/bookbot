def get_word_count(book_text):
    
    book_text = book_text.split()
    word_count = len(book_text)
    number = 0

    return word_count

def get_char_count(book_text):

    book_text = book_text.split()
    characters = {}
    
    for i in book_text:

        word = i.lower()

        for index in range(len(word)):

            char = word[index]

            if word[index] not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

    return characters

def sort_on(items):
    return items["count"]