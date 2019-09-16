
class BloomFilter:
    def __init__(self):
        self.bloom_array = [False] * (2 ** 28)

    def validate(self, word):
        word_value = 0
        for letter in word.lower().strip():
            word_value += (word_value * 22) + abs(ord(letter) - 96)
        return word_value % (2 ** 28)

    def add_word(self, word):
        index = self.validate(word)
        if index > len(self.bloom_array) - 1:
            self.bloom_array = self.bloom_array + ([False] * (index - len(self.bloom_array) + 1))
        self.bloom_array[index] = True

    def has_word(self, word):
        index = self.validate(word)
        if index > len(self.bloom_array):
            return False
        return self.bloom_array[index]

    def load_wordlist(self, file):
        with open(file) as f:
            for word in f.readlines():
                self.add_word(word)
        return

