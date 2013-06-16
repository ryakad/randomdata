#
# Random Data
#
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

import random
import os


class Generator:
    """
    Class for randomly generating content.
    """

    def __init__(self):
        # for make_id()
        self.id = 0
        dictfile = os.path.dirname(__file__) + "/data/dict.txt"
        namefile = os.path.dirname(__file__) + "/data/names.txt"
        self.words = [word.strip() for word in open(dictfile)]
        self.names = [name[0].upper() + name[1:].lower() for name in open(namefile)]

    def _get_words(self, length=0):
        """
        Return an array of words. This allows us to only get words of a
        desired length. The current dictionary supports lengths from 1 to 15
        chars.
        """

        words = self.words[:]
        random.shuffle(words)

        if length == 0:
            return words
        else:
            return [word for word in words if len(word) == length]

    def make_string(self, total_words=0):
        """
        Returns a random string with a given number of words. Uses a
        dictionary to get more easily searchable text.
        """

        if total_words == 0:
            total_words = random.randint(1, 15)

        return ' '.join(self._get_words()[:total_words-1])

    def make_text(self, length=100):
        """
        Returns a paragraph of text to the maximum length of characters
        """

        text = ''
        while True:
            word = self.get_random_word(self._get_words())
            text += word
            text += ' '

            if len(text) == length:
                break

            if (len(text) + 16) > length:
                # need to be more selective
                word_length = length - len(text)
                word = self.get_random_word(self._get_words(word_length))
                text += word
                break

        return text

    def get_random_word(self, words):
        """Returns a random word from within a list"""

        return words[random.randint(0, len(words) - 1)]

    def make_name(self):
        """Returns a random name"""
        return self.names[random.randint(0, len(self.names) - 1)]

    def make_integer(self, length=5):
        """Returns a random positive integer of a specific length"""

        if length < 1:
            return 0

        lowerpoint = '1' + ('0' * (length - 1))
        upperpoint = '9' * length

        return random.randint(int(lowerpoint), int(upperpoint))

    def make_float(self, precision=2, length=3):
        """Returns a random floating point number"""

        base = self.make_integer(length)
        fractal = float(self.make_integer(2)) / (10 ** precision)

        return round(base + fractal, precision)

    def make_id(self):
        """Simulate an auto incrementing id"""

        self.id += 1
        return self.id
