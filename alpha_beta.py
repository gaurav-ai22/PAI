import numpy as np

def minimax(values, depth=0, alpha=float('-inf'), beta=float('inf'), maximizing=True):
    if depth == 3 or depth * 2 >= len(values):
        return values[depth]
    
    if maximizing:
        best = np.NINF
        for i in range(2):
            best = max(best, minimax(values, depth + 1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = np.inf
        for i in range(2):
            best = min(best, minimax(values, depth + 1, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [10, 9, 14, 18, 5, 4, 50, 3]
print("The optimal value is:", minimax(values))
