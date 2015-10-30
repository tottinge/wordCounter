from collections import Counter
from fileinput import FileInput

class WordCounter(object):
    def __init__(self):
        self.counts = Counter()

    def count(self, text):
        for word in text.split():
            for word in self._uncamelCase(word):
                word = word.lower()
                self.counts[word] += 1

    def timesOccurred(self, word):
        return self.counts[word.lower()]

    def _uncamelCase(self, word):
        accumulator = ""
        for (location, letter) in enumerate(word):
            if letter.isalnum():
                if letter.isupper():
                    if accumulator and accumulator[-1].islower():
                        if accumulator:
                            yield accumulator
                            accumulator = ""
                    if accumulator and accumulator[-1].isupper() and (location +1 < len(word)):
                        if word[location+1].islower():
                            yield accumulator
                            accumulator = ""
                accumulator += letter
            else:
                if accumulator:
                    yield accumulator
                accumulator = ""
        if accumulator:
            yield accumulator

    def mostUsedWords(self, number):
        return self.counts.most_common(number)


if __name__ == "__main__":
    counter = WordCounter()
    for line in FileInput():
        counter.count(line)

    index = 0
    for (word,count) in counter.mostUsedWords(100):
        index += 1
        print index, word, count




