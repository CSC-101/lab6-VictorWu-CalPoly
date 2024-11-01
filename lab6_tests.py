from cgitb import reset

import data
import lab6
import unittest
from data import Book


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_alpha_book1(self):
        input = [Book(["Orwell"], "Animal Farm"),
                 Book(["Placer"], "Saw"),
                 Book(["Anna"], "Joy Luck Club"),
                 Book(["Drake"], "Bible")]

        expected = [Book(["Orwell"], "Animal Farm"),
                    Book(["Drake"], "Bible"),
                    Book(["Anna"], "Joy Luck Club"),
                    Book(["Placer"], "Saw")]
        actual = lab6.selection_sort_books(input)
        self.assertEqual(expected, actual)

    def test_alpha_book2(self):
        input = []
        expected = []
        actual = lab6.selection_sort_books(input)
        self.assertEqual(expected, actual)

    # Part 2
    def test_swap_case_1(self):
        input_str = "Apples"
        expected = "aPPLES"
        actual = lab6.swap_case(input_str)
        self.assertEqual(expected, actual)

    def test_swap_case_2(self):
        input = "bAnAnA"
        expected = "BaNaNa"
        actual = lab6.swap_case(input)
        self.assertEqual(expected, actual)

    # Part 3
    def test_str_translate_1(self):
        expected = "allles"
        actual = lab6.str_translate("apples", "l", "p")
        self.assertEqual(expected, actual)

    def test_str_translate_2(self):
        expected = "dadaya"
        actual = lab6.str_translate("papaya", "d", "p")
        self.assertEqual(expected, actual)

    # Part 4
    def test_histogram_1(self):
        input = "skibidi skibidi skibidi skibidi skibidi"
        expected = {"skibidi": 5}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)

    def test_histogram_2(self):
        input = "skibidi skibidi skibidi skibidi skibidi doggo doggo doggo doggo"
        expected = {"skibidi": 5, "doggo": 4}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
