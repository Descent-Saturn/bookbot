def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print (f"--- Begin report of {f.name} ---")
        word_count(file_contents)
def word_count (file_contents):
    total_words = file_contents.split()
    print (f"{len(total_words)} words found in the document")
    character_count(file_contents)
def character_count(file_contents):
    characters_total = {}
    count = 0
    index_value = 0
    string_test = file_contents
    lowered_string = string_test.lower()
    split_test = list(lowered_string)
    passing_list = []
    #passing the string to a new list in order to remove the spaces from the original list
    for i in split_test:
        if i != " ":
            passing_list.append(i)
    for words in passing_list:   #this is the character count code
        if words in characters_total:
            characters_total[words] += 1
        else:
            characters_total[words] = 1
    print ("")
    only_alphabet (characters_total)
def only_alphabet (characters_total):
    mini_dict = []
    for mini, counts in characters_total.items():
        mini_dict.append({mini:counts})
    mini_dict.sort(reverse=True,key=sort_on)
    for alp in mini_dict: #this loops through all the keys in the dictionary.
        for firstk, firstv in alp.items():
            if firstk.isalpha():
                print(f"The '{firstk}' character was found {firstv} times")
    print("--- End report ---")
def sort_on(mini_dict):
    return list(mini_dict.values())[0]
main()
