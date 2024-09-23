def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	word_count(file_contents)
def word_count (file_contents):
    total_words = file_contents.split()
    print (len(total_words))
main()
