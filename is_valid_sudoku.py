# leetcode 36，验证一个数独是否合法，哈希表模拟
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rule_3 3 * 3 * 9 -> bool
        rule_3_table = [[[False] * 9 for i in range(3)] for i in range(3)]
        # rule_1 table 9 * 9
        rule_1_table = [[False] * 9 for i in range(9)]
        # rule_2 table 9 * 9
        rule_2_table = [[False] * 9 for i in range(9)]

        for row, one_row in enumerate(board):
            for column, char in enumerate(one_row):
                if char == '.':
                    continue
                else:
                    num = ord(char) - ord('0')
                    if not rule_1_table[row-1][num-1]:
                        rule_1_table[row-1][num-1] = True
                    else:
                        return False
                    if not rule_2_table[column-1][num-1]:
                        rule_2_table[column-1][num-1] = True
                    else:
                        return False
                    if not rule_3_table[row//3][column//3][num-1]:
                        rule_3_table[row//3][column//3][num-1] = True
                    else:
                        return False
        return True
