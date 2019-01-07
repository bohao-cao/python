class Permutations:
    @staticmethod
    def solution(notes: list, total: int) -> list:
        coefficients = [0] * len(notes)
        starting_idx = -1
        results = []
        Permutations.__recurse(total, notes, coefficients, starting_idx, results)
        return results

    @staticmethod
    def __recurse(total: int, notes: list, coefficient: list, pointer: int, results: list) -> None:
        """

        :param total: total number that can be used
        :param notes: input available notes
        :param coefficient: multiplying factors that is being working on
        :param pointer: which coefficient is being working on
        :param results: list of resulting coefficients
        :return: None
        """
        if pointer == len(coefficient) - 2:
            # calculate total based on the current coefficient
            total_so_far = sum([i[0] * i[1] for i in zip(notes, coefficient)])
            if (total - total_so_far) % notes[-1] == 0:
                coefficient[-1] = int((total - total_so_far) / notes[-1])
                results.append(coefficient[:])
                coefficient[-1] = 0
                return
        else:
            while True:
                Permutations.__recurse(total, notes, coefficient, pointer + 1, results)
                coefficient[pointer + 1] = coefficient[pointer + 1] + 1
                total_so_far = sum([i[0] * i[1] for i in zip(notes, coefficient)])
                if total_so_far > total:
                    coefficient[pointer + 1] = 0
                    return
