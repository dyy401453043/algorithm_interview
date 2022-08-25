# leetcode 127 单词接龙，建图，当权值为1时可以用bfs来计算距离
def word_ladder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    if beginWord not in wordList:
        wordList = wordList + [beginWord]

    idx = 0
    word2idx = {}
    from collections import defaultdict
    adj = defaultdict(list)
    def addWord(word):
        nonlocal idx, word2idx, adj
        word2idx[word] = idx
        idx += 1
        for i in range(len(word)):
            new_word=word[:i]+'*'+word[i+1:]
            if new_word not in word2idx:
                word2idx[new_word] = idx
                idx+=1 
            adj[word2idx[word]].append(word2idx[new_word])
            adj[word2idx[new_word]].append(word2idx[word])
    for word in wordList:
        addWord(word)

    begin_id = word2idx[beginWord]
    from collections import deque
    queue = deque([begin_id])
    distance = {begin_id:0}
    while len(queue) > 0:
        node_idx = queue.popleft()
        for adj_node_idx in adj[node_idx]:
            if adj_node_idx not in distance:
                queue.append(adj_node_idx)
                distance[adj_node_idx] = distance[node_idx] + 1
                if adj_node_idx == word2idx[endWord]:
                    return int(distance[adj_node_idx] / 2) + 1
    return 0

# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog","dot"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(word_ladder(beginWord, endWord, wordList))
