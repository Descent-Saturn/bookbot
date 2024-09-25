def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	word_count(file_contents)
def word_count (file_contents):
    total_words = file_contents.split()
    print (len(total_words))
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
    print (characters_total)
main()
