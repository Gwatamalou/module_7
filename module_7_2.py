
def custom_write(file_name, strings):
    string_positions = {}
    f = open(file_name, 'w', encoding='utf-8')
    x = 1
    for i in strings:
        string_positions[(x, f.tell())] = i
        f.write(f'{i}\n')
        x+=1
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



