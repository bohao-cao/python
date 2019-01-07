import unittest

def recurse(input: list, coefficients: list, i: int, total: int, results: list):
    if i == len(coefficients) - 2:
        total_so_far = sum([i[0] * i[1] for i in zip(input, coefficients)])
        if (total - total_so_far) % input[-1] == 0:
            coefficients[-1] = (int)((total - total_so_far) / input[-1])
            results.append(coefficients[:])
            coefficients[-1] = 0
            return
    else:
        while True:
            recurse(input, coefficients, i + 1, total, results)
            coefficients[i + 1] = coefficients[i + 1] + 1
            total_so_far = sum([i[0] * i[1] for i in zip(input, coefficients)])
            if total_so_far > total:
                coefficients[i + 1] = 0
                return



class TestRecurse(unittest.TestCase):

    def test_1(self):
        input = [50, 30, 15, 10]
        coefficients = [0] * len(input)
        i = -1
        total = 300
        results = []
        recurse(input, coefficients, i, total, results)

        for result in results:
            actual_total = sum([i[0] * i[1] for i in zip(input, result)])
            self.assertEqual(actual_total, total)


    def test_2(self):
        input = [50, 30, 20]
        coefficients = [0] * len(input)
        i = -1
        total = 300
        results = []

        recurse(input, coefficients, i, total, results)

        print(*results, sep="\n")

        for result in results:
            actual_total = sum([i[0] * i[1] for i in zip(input, result)])
            self.assertEqual(actual_total, total)

if __name__ == '__main__':
    unittest.main()
