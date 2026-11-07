"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("Apple"), 2)
        self.assertEqual(hw1.vowel_count("AEIOUaeiou"), 10)
 
    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)
 
    def test_vowel_count_no_vowels(self):
        self.assertEqual(hw1.vowel_count("summer time"), 4)
 
    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        items = [[1], [2, 3], [], [4, 5, 6], [7, 8]]
        self.assertEqual(hw1.short_lists(items), [[2, 3], [7, 8]])
 
    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [], [1, 2, 3]]), [])
        self.assertEqual(hw1.short_lists([]), [])
 
    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[9, 2], [5, 5], [1, 4]]), [[2, 9], [5, 5], [1, 4]])
 
    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual(hw1.ascending_pairs([[9, 2], [3, 1, 2], [], [8]]), [[2, 9], [3, 1, 2], [], [8]])
 
    def test_ascending_pairs_does_not_modify_input(self):
        items = [[9, 2]]
        hw1.ascending_pairs(items)
        self.assertEqual(items, [[9, 2]])
 
    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(1, 20), data.Price(2, 30)), data.Price(3, 50))
 
    def test_add_prices_with_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(3, 75), data.Price(2, 50)), data.Price(6, 25))
 
    def test_add_prices_exactly_100_cents(self):
        self.assertEqual(hw1.add_prices(data.Price(0, 50), data.Price(0, 50)), data.Price(1, 0))
 
    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rectangle = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        self.assertAlmostEqual(hw1.rectangle_area(rectangle), 50)
 
    def test_rectangle_area_negative_coordinates(self):
        rectangle = data.Rectangle(data.Point(-4, 3), data.Point(2, -2))
        self.assertAlmostEqual(hw1.rectangle_area(rectangle), 30)
 
    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        book1 = data.Book(['William Shakespeare', 'Agatha Christie'], 'Hercule Poirot')
        book2 = data.Book(['William Shakespeare'], 'Hamlet')
        book3 = data.Book(['Agatha Christie'], 'Killings')
        books = [book1, book2, book3]
        self.assertEqual(hw1.books_by_author('William Shakespeare', books), [book1, book2])
 
    def test_books_by_author_no_matches(self):
        books = [data.Book(['Agatha Christie'], 'Killings')]
        self.assertEqual(hw1.books_by_author('William Shakespeare', books), [])
        self.assertEqual(hw1.books_by_author('William Shakespeare', []), [])
 
    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rectangle = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        self.assertEqual(hw1.circle_bound(rectangle), data.Circle(data.Point(1, 1), 2 ** 0.5))
 
    def test_circle_bound_non_square_rectangle(self):
        rectangle = data.Rectangle(data.Point(0, 4), data.Point(6, 0))
        self.assertEqual(hw1.circle_bound(rectangle), data.Circle(data.Point(3, 2), 13 ** 0.5))
 
    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [data.Employee('Alice', 10), data.Employee('Bob', 20), data.Employee('Chloe', 30), data.Employee('Diana', 20)]
        self.assertEqual(hw1.below_pay_average(employees), ['Alice'])
 
    def test_below_pay_average_empty_list(self):
        self.assertEqual(hw1.below_pay_average([]), [])
 
    def test_below_pay_average_all_equal(self):
        employees = [data.Employee('Alice', 15), data.Employee('Bob', 15)]
        self.assertEqual(hw1.below_pay_average(employees), [])
 
if __name__ == '__main__':
    unittest.main()
