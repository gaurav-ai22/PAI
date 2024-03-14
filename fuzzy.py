from constraint import Problem

class CrosswordPuzzle:
    def __init__(self, width, height, words):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.words = words

    def fill_puzzle(self):
        problem = Problem()
        problem.addVariables(range(self.width * self.height), self.words)
        
        for i in range(self.width * self.height):
            for j in range(i + 1, self.width * self.height):
                if i // self.width == j // self.width:  # Same row
                    problem.addConstraint(lambda x, y: x != y, (i, j))
                if i % self.width == j % self.width:  # Same column
                    problem.addConstraint(lambda x, y: x != y, (i, j))

        solution = problem.getSolution()

        for position, word in solution.items():
            row = position // self.width
            col = position % self.width
            self.grid[row][col] = word[position]

    def display(self):
        for row in self.grid:
            print(' '.join(row))

# Example usage
words = ['apple', 'banana', 'orange', 'grape', 'lemon']
puzzle = CrosswordPuzzle(10, 10, words)
puzzle.fill_puzzle()
puzzle.display()
