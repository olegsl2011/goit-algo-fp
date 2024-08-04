import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def run_reverse_test_case(self, elements, expected_result):
        lst = LinkedList()
        for element in elements:
            lst.insert_at_end(element)

        lst.reverse()

        self.assertEqual(expected_result, str(lst))

    def test_reverse(self):
        test_cases = [
            ([], ''),
            ([3, 5, -1], '-1 5 3'),
            ([0, 0, 0], '0 0 0'),
            ([None, 0, 0], '0 0 None'),
        ]

        for elements, expected_result in test_cases:
            with self.subTest(elements=elements, expected_result=expected_result):
                self.run_reverse_test_case(elements, expected_result)

    def run_sort_test_case(self, elements, expected_result):
        lst = LinkedList()
        for element in elements:
            lst.insert_at_end(element)

        lst.sort()

        self.assertEqual(expected_result, str(lst))

    def test_sort(self):
        test_cases = [
            ([], ''),
            ([3, 5, -1], '-1 3 5'),
            ([0, 0, 0], '0 0 0'),
            ([0, None, 0], '0 0 None'),
        ]

        for elements, expected_result in test_cases:
            with self.subTest(elements=elements, expected_result=expected_result):
                self.run_sort_test_case(elements, expected_result)

    def run_merge_test_case(self, elements1, elements2, expected_result):
        lst1 = LinkedList()
        for element in elements1:
            lst1.insert_at_end(element)

        lst2 = LinkedList()
        for element in elements2:
            lst2.insert_at_end(element)

        lst1.merge(lst2)

        self.assertEqual(expected_result, str(lst1))

    def test_merge(self):
        test_cases = [
            ([], [], ''),
            ([3, 5, -1], [], '-1 3 5'),
            ([3, 5, -1], [0, 0, 0], '-1 0 0 0 3 5'),
            ([0, 0, 0], [0, 1, 0], '0 0 0 0 0 1'),
            ([0, 0, 0], [0, None, 0], '0 0 0 0 0 None'),
            (["0", "0", "0"], ["0", "1", "0"], '0 0 0 0 0 1'),
        ]

        for elements1, elements2, expected_result in test_cases:
            with self.subTest(elements1=elements1, elements2=elements2, expected_result=expected_result):
                self.run_merge_test_case(elements1, elements2, expected_result)


if __name__ == '__main__':
    unittest.main()
