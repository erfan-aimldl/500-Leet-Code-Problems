# Problem Link : https://leetcode.com/problems/baseball-game/

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        for idx in range(len(operations)):
            if operations[idx] == "+":
                value_1 = record[-1] + record[-2]
                record.append(value_1)
            elif operations[idx] == "D":
                value = record[-1] * 2
                record.append(value)
            elif operations[idx] == "C":
                record.pop()
            else:
                record.append(int(operations[idx]))
        return sum(record)