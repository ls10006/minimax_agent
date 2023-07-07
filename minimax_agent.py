import utils
alpha = -(1e9)
beta = 1e9
class MinimaxAgent:
    def __init__(self, side):
        self.side = side
        self.name = "agent"
        self.opponentSide = "black" if self.side == "white" else "white"

    def evaluate(self, board):
        """
        評估函數
        """
        score = 0
        for x in range(8):
            for y in range(8):
                if board[x][y] == self.side:
                    if x == 0 or y == 0 or x == 7 or y == 7:
                        score += 50
                    if x == 0 and y == 0:
                        score += 800
                    if x == 0 and y ==7:
                        score += 800
                    if x == 7 and y == 0:
                        score += 800
                    if x == 7 and y == 7:
                        score += 800
                    if x == 1 and y == 0 or y == 1 or y == 6 or y == 7:
                        score -= 100
                    if x == 0 and y == 1 or y == 6:
                        score -= 100
                    if x == 6 and y == 0 or y == 1 or y == 6 or y == 7:
                        score -= 100
                    if x == 7 and y == 1 or y == 6:
                        score -= 100
                    score += 1
                elif board[x][y] == self.opponentSide:
                    if x == 0 or y == 0 or x == 7 or y == 7:
                        score -= 50
                    if x == 0 and y == 0:
                        score -= 800
                    if x == 0 and y ==7:
                        score -= 800
                    if x == 7 and y == 0:
                        score -= 800
                    if x == 7 and y == 7:
                        score -= 800
                    if x == 1 and y == 0 or y == 1 or y == 6 or y == 7:
                        score += 100
                    if x == 0 and y == 1 or y == 6:
                        score += 100
                    if x == 6 and y == 0 or y == 1 or y == 6 or y == 7:
                        score += 100
                    if x == 7 and y == 1 or y == 6:
                        score += 100
                    score -= 1
        return score
    
    def minimax(self, board, depth, maximized, alpha, beta):
        if depth == 0 or len(utils.getValidMoves(board, self.side if maximized else self.opponentSide)) == 0:
            return self.evaluate(board), None
       
        if maximized:
            val = float("-inf")
            move = None
            for x, y in utils.getValidMoves(board, self.side): # x, y 是下棋位置的座標
                copyBoard = utils.getBoardCopy(board)
                utils.flip(copyBoard, self.side, x, y)
                child_score, _ = self.minimax(copyBoard, depth-1, False, alpha, beta)
                # 接下來要判斷 child_score 是否比 val 大，如果是的話，就更新 val 和 move，move 是一個 list 或是 tuple
                # START YOUR CODE #
                if child_score > val:
                    val = child_score
                    move = [x, y]
                if val >= beta:
                    break
                alpha = max(alpha, val)

                # END YOUR CODE #

            return val, move
        else:
            val = float("inf")
            move = None
            for x, y in utils.getValidMoves(board, self.opponentSide): # x, y 是下棋位置的座標
                copyBoard = utils.getBoardCopy(board)
                utils.flip(copyBoard, self.opponentSide, x, y)
                child_score, _ = self.minimax(copyBoard, depth-1, True, alpha, beta)           
                # 接下來要判斷 child_score 是否比 val 小，如果是的話，就更新 val 和 move，move 是一個 list 或是 tuple
                # START YOUR CODE #

                if child_score < val:
                    val = child_score
                    move = [x, y]
                if val <= alpha:
                    break
                beta = min(beta, val)

                # END YOUR CODE #
                
            return val, move

    def choose(self, board, valid_moves):
        """
        用最白癡的greedy選擇最佳的走法
        """
        _, bestMove = self.minimax(board, 4, True, alpha, beta)

        return bestMove
