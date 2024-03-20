def main():
    file_url = "books/frankenstein.txt"
    file_contents = read_text_file(file_url)
    text_count = text_counter(file_contents)
    reports = count_letters(file_contents)
    print(f"--- Begin report of {file_url} --- \n")
    for r in reports:
        print(f"The '{list(r.keys())[0]}' character was found {list(r.values())[0]} times")
    print(f"\n --- End report ---")  


def read_text_file(file_url):
    with open(file_url) as f:
        file_contents = f.read()
        return file_contents


def text_counter(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return list(dict.values())[0]


def count_letters(text):
    counter = {}
    for letter in text:
        lowered_letter = letter.lower()
        if lowered_letter in counter and lowered_letter.isalpha():
            counter[lowered_letter] += 1
        elif lowered_letter not in counter and lowered_letter.isalpha():
            counter[lowered_letter] = 1
    result_list = [{key: value} for key, value in counter.items()]
    result_list.sort(reverse=True, key=sort_on)
    return result_list

main()
