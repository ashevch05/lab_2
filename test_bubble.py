import unittest
import test_2 as a
import sys
import io


class BubbleSortTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(a.bubble_sort([]), [])

    def test_reverse_sorted_list(self):
        nums = [5, 4, 3, 2, 1]
        sorted_nums = [1, 2, 3, 4, 5]
        self.assertEqual(a.bubble_sort(nums), sorted_nums)

    def test_list_with_duplicates(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        sorted_nums = [1, 1, 2, 3, 4, 5, 5, 6, 9]
        self.assertEqual(a.bubble_sort(nums), sorted_nums)

    def test_list_with_negative_numbers(self):
        nums = [-3, 1, -4, 1, -5, 9, 2, -6, 5]
        sorted_nums = [-6, -5, -4, -3, 1, 1, 2, 5, 9]
        self.assertEqual(a.bubble_sort(nums), sorted_nums)

    def test_single_element_list(self):
        nums = [42]
        self.assertEqual(a.bubble_sort(nums), nums)

    def test_list_with_floats(self):
        nums = [3.14, 2.71, 1.62, 0.56]
        sorted_nums = [0.56, 1.62, 2.71, 3.14]
        self.assertEqual(a.bubble_sort(nums), sorted_nums)

if __name__ == '__main__':
    unittest.main()
