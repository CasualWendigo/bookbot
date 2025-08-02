import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_on

def get_book_text(file_path):

    print("Analyzing book found at "+ file_path +"...")

    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

def main():

    print("============ BOOKBOT ============")

    try:
        file_path = sys.argv[1]
        contents = get_book_text(file_path)
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

    print("----------- Word Count ----------")
    word_count = get_word_count(contents)
    word_report = f"Found {word_count} total words"
    print(word_report)
    
    print("--------- Character Count -------")
    char_count = get_char_count(contents)
    char_list = [{"key": k, "count": v} for k, v in char_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    
    for i in char_list:
        if i["key"].isalpha():
            char_report = f"{i["key"]}: {i["count"]}"
            print(char_report)



main()