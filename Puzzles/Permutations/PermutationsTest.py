import unittest
from Permutations.Permutations import Permutations


class Test(unittest.TestCase):
    def test_positive_case_1(self):
        notes = [50, 30, 15, 10]
        total = 300
        results = Permutations.solution(notes, total)
        self.__assert(notes, results, total)

    def test_positive_case_2(self):
        notes = [50, 30, 20]
        total = 300

        results = Permutations.solution(notes, total)

        self.__assert(notes, results, total)

    def test_positive_case_3(self):
        notes = [10, 20, 35]
        total = 105

        results = Permutations.solution(notes, total)

        self.__assert(notes, results, total)

    def test_negative_case_1(self):
        notes = [17, 24]
        total = 33

        results = Permutations.solution(notes, total)

        self.assertEqual(len(results), 0)

    def __assert(self, notes: list, results: list, expected_total: int):
        for result in results:
            actual_total = sum([i[0] * i[1] for i in zip(notes, result)])
            self.assertEqual(actual_total, expected_total)

    @staticmethod
    def __pretty_print(to_print: list):
        print(f'Number of items: {len(to_print)} \n')
        print(*to_print, sep="\n")


if __name__ == '__main__':
    unittest.main()
