import random
import time



def time_elapsed(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.5f} seconds")

class KnightsTourLasVegas:
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
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y):
                moves.append((new_x, new_y))
        return moves

    def las_vegas_algorithm(self, p):
        total_squares = self.n * self.n
        success_threshold = int(p * total_squares)
        successful_tours = 0
        total_trials = 100000

        for _ in range(total_trials):
            self.initialize_board()
            self.random_tour(p)

            # Check if the tour is successful
            if self.visited > success_threshold:
                successful_tours += 1

        print(f"--- p = {p} ---")
        print(f"Las Vegas Algorithm With p = {p}")
        print(f"Number of successful tours: {successful_tours}")
        print(f"Number of trials: {total_trials}")
        print(f"Probability of a successful tour: {successful_tours / total_trials}")

    def initialize_board(self):
        self.board = [[-1] * self.n for _ in range(self.n)]
        self.visited = 0

    def random_tour(self, p):
        current_x, current_y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)

        while self.visited < p * self.n * self.n:
            legal_moves = self.get_legal_moves(current_x, current_y)

            if not legal_moves:
                break

            next_move = random.choice(legal_moves)
            current_x, current_y = next_move

            self.visited += 1
            self.board[current_x][current_y] = self.visited


# Example usage:
n = 8  # Chessboard size
knights_tour_lv = KnightsTourLasVegas(n)

# Measurements for p=0.7
time_elapsed(knights_tour_lv.las_vegas_algorithm, p=0.7)

# Measurements for p=0.8
time_elapsed(knights_tour_lv.las_vegas_algorithm, p=0.8)
def time_elapsed(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.5f} seconds")

# Measurements for p=0.85
time_elapsed(knights_tour_lv.las_vegas_algorithm, p=0.85)
