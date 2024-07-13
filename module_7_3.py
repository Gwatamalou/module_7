REMOVE = dict.fromkeys(map(ord, ',.=!?;:'))
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}

        for f in self.file_names:
            with open(f, 'r', encoding='utf-8') as sr:
                a = sr.read().lower().translate(REMOVE).split()
                all_words[f] = list(x for x in a if x not in '-')

        return all_words

    def find(self, word):
        a = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words: a[name] = words.index(word.lower())+1
        return a

    def count(self, word):
        a = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words: a[name] = words.count(word.lower())
        return a



finder1 = WordsFinder('test1.txt')
print(finder1.get_all_words()) # Все слова
print(finder1.find('TEXT')) # 3 слово по счёту
print(finder1.count('teXT')) # 4 слова teXT в тексте всего



finder2 = WordsFinder('test2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
