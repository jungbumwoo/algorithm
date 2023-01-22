from dataclasses import dataclass
from typing import List, Optional, Tuple
from collections import deque
import unittest


# https://leetcode.com/problems/surrounded-regions/

'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        edge_zeros = []
        zeros = set()
        last_x_index = len(board) - 1
        last_y_index = len(board[0]) - 1

        for i in range(max(len(board), len(board[0]))):
            if i < len(board[0]):
                if board[0][i] == "O":
                    edge_zeros.append((0, i))
                if board[last_x_index][i] == "O":
                    edge_zeros.append((last_x_index, i))
            if i < len(board):
                if board[i][0] == "O":
                    edge_zeros.append((i, 0))
                if board[i][last_y_index] == "O":
                    edge_zeros.append((i, last_y_index))

        dx = (0, 0, 1, -1)
        dy = (1, -1, 0, 0)
        
        queue = deque(edge_zeros)
        while queue:
            x, y = queue.popleft()
            zeros.add((x, y))
        
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                    continue
                if (nx, ny) in zeros:
                    continue
                
                if board[nx][ny] == "O":
                    queue.append((nx, ny))

        for p in range(len(board)):
            for q in range(len(board[0])):
                if board[p][q] == "O" and (p, q) not in zeros:
                    board[p][q] = "X"
        return board

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            board: List[List[str]]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]),
                expect=[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
            ),
            TestCase(
                name="test 2",
                input=Args(board = [["X"]]),
                expect=[["X"]]
            ),
            TestCase(
                name="test 3",
                input=Args(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]),
                expect=[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(board=c.input.board)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()