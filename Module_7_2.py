def custom_write(file_name, strings):
	strings_positions = {}
	file = open(file_name, 'a', encoding='utf-8')
	num_str = 1
	for i in strings:
		b = file.tell()
		item = (num_str, b)
		strings_positions[item] = i
		file.write(i+ '\n')
		num_str += 1
	file.close()
	return strings_positions

info = [
	'Text for tell.',
	'Используйте кодировку utf-8.',
	'Because there are 2 languages!',
	'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
	print(elem)