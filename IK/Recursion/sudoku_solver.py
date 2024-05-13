"""
Author: Soumil Ramesh Kulkarni
Date: 05.12.2024

Question:
Given a partially filled two-dimensional array, fill all the unfilled cells such that each row,
each column and each 3 x 3 subgrid (as highlighted below by bolder lines) has every digit from 1 to 9 exactly once.

Unfilled cells have a value of 0 on the given board.

Example one

{
"board": [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
}
Output:

[
[8, 4, 9, 1, 6, 3, 5, 7, 2],
[3, 1, 5, 2, 8, 7, 4, 9, 6],
[7, 6, 2, 4, 9, 5, 1, 8, 3],
[1, 5, 3, 9, 4, 6, 7, 2, 8],
[2, 8, 7, 3, 5, 1, 6, 4, 9],
[4, 9, 6, 8, 7, 2, 3, 5, 1],
[5, 7, 8, 6, 1, 9, 2, 3, 4],
[6, 3, 4, 5, 2, 8, 9, 1, 7],
[9, 2, 1, 7, 3, 4, 8, 6, 5]
]

Notes
You can assume that any given puzzle will have exactly one solution.

Constraints:

Size of the input array is exactly 9 x 9
0 <= value in the input array <= 9
"""

import copy


def solve_sudoku_puzzle(board):
    def constructCandidateState(board):
        state = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]
        changed = [[False] * 9 for _ in range(9)]

        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val > 0:
                    add_value_to_state(state, changed, x, y, val)
        return state, changed

    state, changed = constructCandidateState(board)
    done, stateOut = pruningHelper(state, changed)

    printCandidates(stateOut)
    countSet = 0
    countSetEach = [sum([len(s) == 1 for s in row]) for row in stateOut]

    return [[list(a)[0] for a in row] for row in stateOut]


def listIdentifiedSites(state, changed):
    out = []
    for y, row in enumerate(state):
        for x, val in enumerate(row):
            if changed[y][x] and len(val) == 1:
                out += [(y, x, list(val)[0])]

    return out


def pruningHelper(state, changed):
    deductiveIter(state, changed)
    done, invalid = getStateHealth(state)
    if done or invalid:
        return done, state

    priorityList = [[] for _ in range(10)]
    goFast = True
    if goFast:
        for y in range(9):
            for x in range(9):
                if len(state[y][x]) > 1:
                    priorityList[len(state[y][x])] += [(y, x)]

        for events in priorityList:

            for i in range(len(events)):
                y, x = events[i]

                for val in state[y][x]:
                    stateNew = copy.deepcopy(state)
                    changedNew = copy.deepcopy(changed)
                    stateNew[y][x] = {val}
                    changedNew[y][x] = True

                    done, stateOut = pruningHelper(stateNew, changedNew)
                    if done:
                        return done, stateOut
    else:
        for y in range(9):
            for x in range(9):
                if len(state[y][x]) > 1:
                    for val in state[y][x]:
                        stateNew = copy.deepcopy(state)
                        changedNew = copy.deepcopy(changed)
                        stateNew[y][x] = {val}
                        changedNew[y][x] = True

                        done, stateOut = pruningHelper(stateNew, changedNew)
                        if done:
                            return done, stateOut

    return False, state

    pass


def getStateHealth(state):
    countSet = sum([sum([len(s) == 1 for s in row]) for row in state])
    countInvalid = sum([sum([len(s) == 0 for s in row]) for row in state])
    done = countSet == 81
    invalid = countInvalid > 0
    return done, invalid


def argsort(x):
    return [y for _, y in sorted(zip(x, range(len(x))))]


def add_value_to_state(state, changed, x, y, val):
    didSomething = state[y][x] != {val}
    state[y][x] = {val}
    changed[y][x] = False
    for xWipe in range(9):
        if (y, xWipe) != (y, x):
            try:
                state[y][xWipe].remove(val)
                changed[y][xWipe] = True
                didSomething = True
            except KeyError:
                pass
    for yWipe in range(9):
        if (yWipe, x) != (y, x):
            try:
                state[yWipe][x].remove(val)
                changed[yWipe][x] = True
                didSomething = True
            except KeyError:
                pass

    boxIdX = x // 3
    boxIdY = y // 3
    for xWipe in range(boxIdX * 3, boxIdX * 3 + 3):
        for yWipe in range(boxIdY * 3, boxIdY * 3 + 3):
            if (yWipe, xWipe) != (y, x):
                try:
                    state[yWipe][xWipe].remove(val)
                    changed[yWipe][xWipe] = True
                    didSomething = True

                except KeyError:
                    pass


def deductiveIter(state, changed):
    iterId = 0
    while True:
        changes = listIdentifiedSites(state, changed)
        changes += findSingleCandidateRows(state)
        changes += findSingleCandidateCols(state)
        changes += findSingleCandidateBoxes(state)

        if not changes: break

        for y, x, val in changes:
            add_value_to_state(state, changed, x, y, val)
        iterId += 1
        if iterId > 1000:
            print('infinite loop..')
            break
    return state, changed


def getCol(state, colId):
    return [state[i][colId] for i in range(len(state))]


def getBox(state, boxX, boxY):
    return [state[i][boxX * 3:boxX * 3 + 3] for i in range(boxY * 3, boxY * 3 + 3)]


def findSingleCandidateRows(state):
    out = []
    for rowId in range(len(state)):
        for val in range(1, 10):
            if {val} in state[rowId]: continue
            indMatch = None
            gotMultipleMatches = False
            for colId in range(9):
                if val in state[rowId][colId]:
                    if indMatch is None:
                        indMatch = colId
                    else:
                        gotMultipleMatches = True
                        break
            if not gotMultipleMatches and indMatch is not None:
                out += [(rowId, indMatch, val)]

    return out


def findSingleCandidateCols(state):
    out = []
    for colId in range(len(state)):
        colThis = getCol(state, colId)
        for val in range(1, 10):
            if {val} in colThis: continue
            indMatch = None
            gotMultipleMatches = False
            for rowId in range(9):
                if val in colThis[rowId]:
                    if indMatch is None:
                        indMatch = rowId
                    else:
                        gotMultipleMatches = True
                        break
            if not gotMultipleMatches and indMatch is not None:
                out += [(indMatch, colId, val)]
    return out


def findSingleCandidateBoxes(state):
    out = []
    for boxX in range(3):
        for boxY in range(3):
            boxThis = getBox(state, boxX, boxY)
            boxVec = [v for row in boxThis for v in row]
        for val in range(1, 10):
            if {val} in boxVec: continue
            indMatch = None
            gotMultipleMatches = False
            for rowId in range(9):
                if val in boxVec[rowId]:
                    if indMatch is None:
                        indMatch = rowId
                    else:
                        gotMultipleMatches = True
                        break
            if not gotMultipleMatches and indMatch is not None:
                outY = (indMatch // 3) + boxY * 3
                outX = (indMatch % 3) + boxX * 3
                out += [(outY, outX, val)]
    return out


def printCandidates(state):
    for row in state: print(row)
    pass

    return []
