# leetcode 30, 匹配题，当匹配溢出时，把已匹配部分的前缀作删减
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from copy import copy

        if len(words) == 0:
            return 0
        total = len(words[0]) * len(words)
    
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict[word] + 1 if word in words_dict else 1
        
        step = len(words[0])
        result = []
        for i in range(step):
            count = 0
            temp_words_dict = copy(words_dict)

            while i < len(s):
                word = s[i:i+step]
                if word in temp_words_dict:
                    if temp_words_dict[word] > 0:
                        temp_words_dict[word] -= 1
                        count += 1
                    else:
                        # 溢出了, 把不等于该单词的前缀都舍掉
                        j = i-count*step
                        while s[j:j+step] != word:
                            temp_words_dict[s[j:j+step]] += 1
                            count -= 1
                            j += step
                    if count == len(words):
                        result.append(i+step-total)
                else:
                    count = 0
                    temp_words_dict = copy(words_dict)
                i = i + step
        return result
                
