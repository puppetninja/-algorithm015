from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        word_pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                word_pattern = word[:i] + '*' + word[i+1:]
                word_pattern_dict[word_pattern].append(word)

        visited = {beginWord: True}
        queue = [(beginWord, 1)]
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                next_word_pattern = current_word[:i] + '*' + current_word[i+1:]
                for next_word in word_pattern_dict[next_word_pattern]:
                    if next_word == endWord:
                        return level + 1

                    if next_word not in visited:
                        visited[next_word] = True
                        queue.append((next_word, level+1))

        return 0
