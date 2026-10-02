class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        for op in operations:
            print(score_stack)
            if op not in {'+', 'D', 'C'}:
                score_stack.append(int(op))
            if op == '+':
                score_stack.append(score_stack[-1]+score_stack[-2])
            if op == 'D':
                score_stack.append(2 * score_stack[-1])
            if op == 'C':
                score_stack.pop()
        return sum(score_stack)
            