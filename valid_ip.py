class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def legal_number(number):
            return len(number) <= 3 and (number[0] != '0' or len(number) == 1) and int(number) <= 255
        result = []
        def dfs(temp_result, string):
            if len(temp_result) == 4 and string == '':
                if all([legal_number(number) for number in temp_result]):
                    result.append('.'.join(temp_result))
                else:
                    return
            else:
                if len(temp_result) > 4 or len(string) > 12 or (len(temp_result) < 4 and string==''):
                    return
                else:
                    dfs(temp_result+[string[0]], string[1:])
                    if len(temp_result) > 0:
                        dfs(temp_result[:-1] + [temp_result[-1]+string[0]], string[1:])
        dfs([], s)
        return result
