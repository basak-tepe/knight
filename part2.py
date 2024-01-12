import random

class KnightsTour:
    def __init__(self, n):
        self.n = n
        self.board = [[-1] * n for _ in range(n)]
        self.visited = 0

    def is_valid_move(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == -1

    def get_legal_moves(self, x, y):
        moves = []
        possible_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        for dx, dy in possible_moves:
            new_x, new_y = x + dx, y + dy # New position
            if self.is_valid_move(new_x, new_y):
                moves.append((new_x, new_y))
        return moves

    def las_vegas_algorithm(self, p, k):
        successful_tours = 0
        total_trials = 100000
        successful_tours_threshold = int(p * total_trials) # Stop the loop if the number of successful tours exceeds this threshold

        for _ in range(total_trials):
            self.initialize_board()
            self.random_k_moves(k)

            # Check if the initial percentage of visited squares is less than 'p'
            initial_percentage = self.visited / (self.n * self.n)
            if initial_percentage < p:
                # Start backtracking to complete the tour
                if self.backtrack_dfs(0, 0):
                    successful_tours += 1

                # Break the loop if the number of successful tours exceeds the threshold
                if successful_tours > successful_tours_threshold:
                    break

        print(f"--- p = {p} ---")
        print(f"LasVegas Algorithm With p = {p}, k = {k}")
        print(f"Number of successful tours: {successful_tours}")
        print(f"Number of trials: {total_trials}")
        print(f"Probability of a successful tour: {successful_tours / total_trials}")

    def initialize_board(self):
        self.board = [[-1] * self.n for _ in range(self.n)]
        self.visited = 0

    def random_k_moves(self, k):
        current_x, current_y = 0, 0

        for _ in range(k):
            legal_moves = self.get_legal_moves(current_x, current_y)

            if not legal_moves:
                break

            next_move = random.choice(legal_moves)
            current_x, current_y = next_move

            self.visited += 1
            self.board[current_x][current_y] = self.visited

    def backtrack_dfs(self, x, y):
        stack = [(x, y)]
        visited_count = 1

        while stack:
            current_x, current_y = stack[-1]
            legal_moves = self.get_legal_moves(current_x, current_y)

            if not legal_moves:
                # No legal moves from the current position, backtrack
                self.visited -= 1
                self.board[current_x][current_y] = -1
                stack.pop()
            else:
                # Choose the next move and update the board
                next_move = legal_moves.pop()
                next_x, next_y = next_move
                stack.append((next_x, next_y)) # Push the next move to the stack
                self.visited += 1 # Update the number of visited squares
                self.board[next_x][next_y] = self.visited # Update the board
                visited_count += 1 # Update the number of visited squares

                # Check if the tour is complete
                if visited_count == self.n * self.n:
                    return True

        return False

# Example usage:
n = 8  # Chessboard size
print("hello")
knights_tour = KnightsTour(n)
knights_tour.las_vegas_algorithm(p=0.7, k=0)
print("0.7 has k=0 finished")
print("result table is: ")
print(knights_tour.board)
#knights_tour.las_vegas_algorithm(p=0.7, k=2)
print("0.7 has k=2 finished")
#knights_tour.las_vegas_algorithm(p=0.7, k=3)
print("0.7 has k=3 finished")
#knights_tour.las_vegas_algorithm(p=0.8, k=0)
print("0.8 has k=0 finished")
print("result table 2 is: ")
print(knights_tour.board)
knights_tour.las_vegas_algorithm(p=0.8, k=2)
print("0.8 has k=2 finished")
# Add more cases as needed
