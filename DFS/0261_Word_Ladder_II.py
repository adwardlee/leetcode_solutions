'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 7
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.output = []
        self.length = 1e10
        if len(wordList) == 0:
            return []
        dicts = set(wordList) | set([beginWord])
        wordlen = len(beginWord)
        word_hash = {}
        graph_hash = {}
        visited = {}
        for x in dicts:
            for idx in range(wordlen):
                tmp = x[:idx] + '*' + x[idx+1:]
                if tmp not in word_hash:
                    word_hash[tmp] = [x]
                else:
                    word_hash[tmp].append(x)
        for key in word_hash.keys():
            for i, value in enumerate(word_hash[key]):
                visited[value] = 0
                remain_list = word_hash[key][:i] + word_hash[key][i+1:]
                if value not in graph_hash:
                    graph_hash[value] = remain_list
                else:
                    for x in remain_list:
                        if x not in graph_hash[value]:
                            graph_hash[value].append(x)
        #self.bfs(deque([[start, [start], {start:1}]]), graph_hash, end)
        self.bfs(deque([[beginWord, [beginWord]]]), graph_hash, endWord)
        #self.backtracking(start, [start], graph_hash, visited, end)
        return self.output
    
    def bfs(self, stack, graph_hash, end):
        minLength = 1e10
        visited = set([stack[0][0]])
        flag = False

        while stack:
            #node, beforewords, cur_visited = stack.popleft()
            local_visited = set()
            length = len(stack)
            for i in range(length):
                node, beforewords = stack.popleft()
                if len(beforewords) >= minLength:
                    break
                for neighbor in graph_hash[node]:
                    if neighbor == end:
                        self.output.append(beforewords + [neighbor])
                        if flag == False:
                            flag = True
                            minLength = len(beforewords) + 1
                        break
                    if neighbor not in visited:#cur_visited:
                        local_visited.add(neighbor)
                        stack.append([neighbor, beforewords + [neighbor]])
                    #tmp = cur_visited.copy()
                    #tmp[neighbor] = 1
                    #stack.append([neighbor,beforewords + [neighbor], tmp])
            visited = visited | local_visited
        if flag == False:
            self.output = []
        #print('min length ', minLength, flush=True)
        return