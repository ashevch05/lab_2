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


    def test_exit_code(self):
        nums_exit_code_0 = [2, 4, 5, 2, 1, 7.3, 3]
        exit_code_0 = a.main(nums_exit_code_0)[0]
        self.assertEqual(exit_code_0, 0)

    def test_stdin(self):
        test_cases = [
            ("10 -5 3.14 0 7.2", [-5, 0, 3.14, 7.2, 10]),
            ("-2.5 4.1 0.0 9.8 -1.2", [-2.5, -1.2, 0.0, 4.1, 9.8]),
            ("42 -10 5 3 8 2", [-10, 2, 3, 5, 8, 42]),
            ("1.23 4.56 7.89", [1.23, 4.56, 7.89]),
            ("-3 -1 -5 -2 -4", [-5, -4, -3, -2, -1]),
            ("6.28 3.14 2.71 1.62", [1.62, 2.71, 3.14, 6.28]),
            ("-7 0 5 10 -3 2", [-7, -3, 0, 2, 5, 10])
        ]

        for test_input, expected_result in test_cases:
            with self.subTest(test_input=test_input, expected_result=expected_result):
                sys.stdin = io.StringIO(test_input)
                exit_code, sorted_numbers = a.main()
                self.assertEqual(exit_code, 0)
                self.assertEqual(sorted_numbers, expected_result)

if __name__ == '__main__':
    unittest.main()
