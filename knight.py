import random
import time

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

    def las_vegas_algorithm(self, p, log_file):
        total_squares = self.n * self.n
        success_threshold = int(p * total_squares)
        successful_tours = 0
        total_trials = 100000

        with open(log_file, "w") as file:
            for trial in range(1, total_trials + 1):
                self.initialize_board()
                current_x, current_y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
                self.board[current_x][current_y] = 0
                self.visited = 1

                file.write(f"Run {trial}: starting from ({current_x},{current_y})\n")

                while self.visited < success_threshold:
                    legal_moves = self.get_legal_moves(current_x, current_y)

                    if not legal_moves:
                        break

                    next_move = random.choice(legal_moves)
                    current_x, current_y = next_move

                    self.visited += 1
                    self.board[current_x][current_y] = self.visited

                    # Write the tour steps to the log file inside the loop
                    file.write(f"Stepping into ({current_x},{current_y})\n")

                # Write the result of the run to the log file outside the loop
                result = "Successful" if self.visited >= success_threshold else "Unsuccessful"
                file.write(f"{result} - Tour length: {self.visited}\n")

                # Write the board to the log file in a grid format
                for row in self.board:
                    file.write(" ".join(f"{square:2d}" for square in row) + "\n")


                if self.visited >= success_threshold:
                    successful_tours += 1

        print(f"--- p = {p} ---")
        print(f"Number of successful tours: {successful_tours}")
        print(f"Number of trials: {total_trials}")
        print(f"Probability of a successful tour: {successful_tours / total_trials}")

    def initialize_board(self):
        self.board = [[-1] * self.n for _ in range(self.n)]
        self.visited = 0



def time_elapsed(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.5f} seconds")

# Example usage:
n = 8  # Chessboard size
log_file1 = "results_0.7.txt"  # Specify the log file name
log_file2 = "results_0.8.txt"  # Specify the log file name
log_file3 = "results_0.85.txt"  # Specify the log file name

knights_tour_lv = KnightsTourLasVegas(n)

# Run the Las Vegas algorithm with p=0.7 and log to file
time_elapsed(knights_tour_lv.las_vegas_algorithm, p=0.7, log_file=log_file1)

# Run the Las Vegas algorithm with p=0.8 and log to file
time_elapsed(knights_tour_lv.las_vegas_algorithm, p=0.8, log_file=log_file2)

# Run the Las Vegas algorithm with p=0.85 and log to file
time_elapsed(knights_tour_lv.las_vegas_algorithm, p=0.85, log_file=log_file3)
