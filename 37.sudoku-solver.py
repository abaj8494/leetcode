from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        N = len(board)
        visited = set()
        empties = []

        def hashBoard():
            """
            total = 0
            for row in range(N):
                for col in range(N):
                    total += board[row][col]
            visited.add(total)
            """
            # again, a garbage hash.
            hashed_board = "".join("".join(i for i in row) for row in board)

            print("hashed board:", hashed_board)
            return hashed_board

        def fullGroup(group: List[str]) -> bool:
            uniques = list(set(group))
            if len(uniques) != N:
                return False
            return True

        def checkGroup(group: List[str]) -> bool:
            uniques = list(set(group))
            counts = {s: group.count(s) for s in uniques}
            #del counts['.']  # we don't care about how many empties
            counts.pop('.', None)
            if any(value > 1 for value in counts.values()):
                return False
            if any(int(key) > 9 or int(key) < 1 for key in counts.keys()):
                return False
            return True

        def isSolved():
            """
            rowSum = 0
            for row in board:
                if sum(row) != WIN_SUM:
                    return False
            """
            # this is a stupid way to check! you can literally do 9 5's
            ###########################################################
            # check rows:
            for row in board:
                if not (checkGroup(row) and fullGroup(row)):
                    return False

            # check columns:
            for i in range(N):
                col = [row[i] for row in board]
                if not (checkGroup(col) and fullGroup(col)):
                    return False

            # check grids:
            for row_offset in range(0, N, 3):
                for col_offset in range(0, N, 3):
                    subgrid = []
                    for r in range(row_offset, row_offset + 3):
                        for c in range(col_offset, col_offset + 3):
                            subgrid.append(board[r][c])
                    if not (checkGroup(subgrid) and fullGroup(subgrid)):
                        return False
            return True

        def validMove(board_state: List[List[str]], pos: tuple) -> List[int]:
            curr_num = board_state[pos[0]][pos[1]]
            valid_moves = []
            for i in range(1, N+1):  # checking candidates
                board_state[pos[0]][pos[1]] = str(i) # set the candidate in board
                row = board_state[pos[0]] # save row as var, with new candidate
                col = [r[pos[1]] for r in board_state] # set col with candidate
                subgrid = []
                row_offset = (pos[0] // 3) * 3
                col_offset = (pos[1] // 3) * 3
                for r in range(row_offset, row_offset + 3):
                    for c in range(col_offset, col_offset + 3):
                        subgrid.append(board_state[r][c])

                if not checkGroup(row):
                    board_state[pos[0]][pos[1]] = curr_num # reset the board_state
                    continue  # the i value does not work.
                # check col
                if not checkGroup(col):
                    board_state[pos[0]][pos[1]] = curr_num # reset the board_state
                    continue  # the i value does not work.
                # check containing subgrid
                if not checkGroup(subgrid):
                    board_state[pos[0]][pos[1]] = curr_num # reset the board_state
                    continue  # the i value does not work.
                # position is valid
                board_state[pos[0]][pos[1]] = curr_num # reset the board_state
                valid_moves.append(str(i))
            return valid_moves

        def find_empties():
            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if col == '.':
                        empties.append((i, j))

        def dfs():
            dfs_rec(board, empties.pop(0))

        def dfs_rec(board_state: List[List[str]], pos: tuple):
            print(board)
            if isSolved():
                return True
            hashed_board = hashBoard()
            if hashed_board in visited:
                return False
            visited.add(hashed_board)
            valid_moves = validMove(board_state, pos) # list of strings

            for move in valid_moves:
                original = board_state[pos[0]][pos[1]]
                board_state[pos[0]][pos[1]] = move
                dot = empties.pop(0)
                if dfs_rec(board_state, dot):
                    return True
                else:
                    # undo move
                    empties.append(dot)
                    board_state[pos[0]][pos[1]] = original
            #return True


        find_empties()
        while not isSolved():
            dfs()
            break

if __name__ == "__main__":
    S = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(board)
    S.solveSudoku(board)
