class WordsFinder:
	def __init__(self, *args):
		self.file_names = list(args)

	def get_all_words(self):
		punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

		def remove_punctuation(text):
			for symbol in punctuation:
				text = text.replace(symbol, '')
			return text

		all_words = {}
		for i in self.file_names:
			with open(i, 'r', encoding='utf-8') as file:
				content = file.read().lower()
				content = remove_punctuation(content)
				words = content.split()
				all_words[i] = words
		return all_words

	def find(self, word):
		word = word.lower()
		rez_word = {}
		for name, words in self.get_all_words().items():
			if word in words:
				rez_word[name] = words.index(word) + 1
		return rez_word

	def count(self, word):
		word = word.lower()
		rez_word = {}
		for name, words in self.get_all_words().items():
			if word in words:
				rez_word[name] = words.count(word)
		return rez_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


