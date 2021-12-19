class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
            
        cur.is_word = True
        
    def exists(self, word):
        cur = self.root
        
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
            
        return cur.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        Implement trie and make a trie from every word in words.
        
        For each cell in the board, if the letter exists in the top level of the trie, we traverse to see if words exist.
        
        Traverse the trie with a dfs, but only advance if children are adjacent to your current cell.
        Use backtracking (set a cell as used, recurse, then unset) to search the board without repeating cells.
        We are traversing the trie and the board at the same time, but only exploring board paths that exist in the trie.
        If the current TrieNode is a word, it must go in results, because we only explore word paths from the wordTrie.
        
        For complexity, call "c" the sum of word lengths in words.
        Call "m" the board width and "n" the board height.
        Call "L" the length of the longest word in words.
        
        Building trie: O(number of total characters in words), aka O(c) time and space
        
        Traversing from one cell: worst case for longest word, we start with 4 direction options then have 3 at each step. This comes out to O(4*3^(L-1)). O(mn) space for recursion stack.
        
        
        Traversing all cells: O(mn * 4 * 3^(L-1)) time, O(mn) space based on the space for traversal from one cell.
        
        The time for traversing the cells overwhelms the time to build the trie, based on the constraint numbers in the description.
        
        Time: O(mn * 4 * 3^(L-1))
        Space: O(c) + O(mn)
        '''
        
        USED = '#'
        wordTrie = Trie()
        
        for word in words:
            wordTrie.insert(word)
            
        result = set()
            
        def backtrack(node, prefix, i, j):
            if node.is_word:
                result.add(prefix)

            for di, dj in ((0,1), (0,-1), (-1,0), (1,0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] in node.children:
                    tmp = board[ni][nj]
                    board[ni][nj] = USED
                    backtrack(node.children[tmp], prefix + tmp, ni, nj)
                    board[ni][nj] = tmp
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in wordTrie.root.children:
                    tmp = board[i][j]
                    board[i][j] = USED
                    backtrack(wordTrie.root.children[tmp], tmp, i, j)
                    board[i][j] = tmp
                    
        return list(result)