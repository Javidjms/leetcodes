from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mapping = {
            1: [],
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        curr_mappings = []
        for digit in digits:
            curr_mappings.append(mapping[int(digit)])

        output = []
        for prod in product(*curr_mappings):
            output.append("".join(prod))
        return output