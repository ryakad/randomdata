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

import unittest
from generator import Generator


class GeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.generator = Generator()

    def test_get_words_returns_valid_length(self):
        words = self.generator._get_words(10)
        self.assertEquals(len(words), len([i for i in words if len(i) == 10]))

    def test_make_string_valid_length(self):
        string = self.generator.make_string(10)
        # a 10 word string should have 9 spaces
        self.assertEquals(9, len(string.split(' ')))

    def test_get_words_always_different_order(self):
        words1 = self.generator._get_words()
        words2 = self.generator._get_words()

        self.assertNotEquals(words1[:10], words2[:10])

    def test_make_invalid_integer_returns_0(self):
        integer = self.generator.make_integer(0)
        self.assertEquals(0, integer)

        integer = self.generator.make_integer(-1)
        self.assertEquals(0, integer)


if __name__ == "__main__":
   unittest.main()
