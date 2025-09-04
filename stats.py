def get_num_words(contents):
    return len(contents.split())

def get_char_count(contents):
    list_of_chars = list(contents.lower())
    set_of_chars = list(set(list_of_chars))
    result = {}
    for char in set_of_chars:
        char_count = list_of_chars.count(char)
        result[char] = char_count
    return result

def sort_on(item):
    return item["num"]

def print_report(contents, file_path):    
    num_words = get_num_words(contents)
    char_count = get_char_count(contents)
    keys_from_iteration = [key for key in char_count]
    result = []
    for key in keys_from_iteration:
        if key.isalpha():
            result.append({"char": key, "num": char_count[key]})
    result.sort(reverse=True, key=sort_on)
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in result:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")