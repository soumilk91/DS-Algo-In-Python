"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
You are given a dictionary set dictionary that contains dictionaryCount distinct words and a matrix mat of size n * m.
Your task is to find all possible words that can be formed by a sequence of adjacent characters in the matrix mat.
Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of the same cell of the matrix.

Example
{
"dictionary": ["bst", "heap", "tree"],
"mat": ["bsh", "tee", "arh"]
}
Output:

["bst", "tree"]
The input matrix is represented below:

bsh
tee
arh

Assume here top left-most corner is at (0,0) and bottom right-most corner is (2,2).
Presence of "bst" is marked bold in the below representation:
(0,0) -> (0,1) -> (1,0)

bsh
tee
arh

Presence of "tree" is marked bold in the below representation:
(1,0) -> (2,1) -> (1,1) -> (1,2)

bsh
tee
arh
"""

def boggle_solver(dictionary, mat):

    board, words = mat, dictionary
    board = [[c for c in row] for row in board]

    WORD_KEY = '$'

    trie = {}
    for word in words:
        node = trie
        for letter in word:
            node = node.setdefault(letter, {})
        node[WORD_KEY] = word

    rowNum = len(board)
    colNum = len(board[0])

    matchedWords = []

    def backtracking(row, col, parent):

        nonlocal board

        letter = board[row][col]
        currNode = parent[letter]

        word_match = currNode.pop(WORD_KEY, False)
        if word_match:
            matchedWords.append(word_match)

        board[row][col] = '#'

        for (rowOffset, colOffset) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            newRow, newCol = row + rowOffset, col + colOffset
            if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                continue
            if not board[newRow][newCol] in currNode:
                continue
            backtracking(newRow, newCol, currNode)

        board[row][col] = letter

        if not currNode:
            parent.pop(letter)

    for row in range(rowNum):
        for col in range(colNum):
            if board[row][col] in trie:
                backtracking(row, col, trie)

    return matchedWords