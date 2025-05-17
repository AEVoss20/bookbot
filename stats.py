def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def counter(file_contents):
    char_count = {}
    lowercase = file_contents.lower()
    for char in lowercase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count