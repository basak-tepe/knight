import random
import time



def time_elapsed(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    #print(f"Time taken: {elapsed_time:.5f} seconds") just for report purposes , not necessary

class KnightsTour: #this class is for the las vegas algorithm with k moves
    def __init__(self, n):
        self.n = n
        self.board = [[-1] * n for _ in range(n)]
        self.visited = 0 #this is the number of visited squares

    def is_valid_move(self, x, y): #this function checks if the move is valid
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
        successful_tours_threshold = int(p * total_trials) 
        #then I gave up from this threshold 
        for _ in range(total_trials):
            self.initialize_board()
            last_coors=self.random_k_moves(k)

            # Check if the initial percentage of visited squares is less than 'p'
            initial_percentage = self.visited / (self.n * self.n)
            if initial_percentage < p:
                # Start backtracking to complete the tour
                x_last = last_coors[0]
                y_last=last_coors[1]
                #print("last coors are: ",x_last,"and",y_last)
                if self.backtrack_dfs(x_last, y_last,p): 
                    successful_tours += 1

        print(f"--- p = {p} ---")
        print(f"LasVegas Algorithm With p = {p}, k = {k}")
        print(f"Number of successful tours: {successful_tours}")
        print(f"Number of trials: {total_trials}")
        print(f"Probability of a successful tour: {successful_tours / total_trials}")
        print() 

    def initialize_board(self):
        self.board = [[-1] * self.n for _ in range(self.n)]
        self.visited = 0

    def random_k_moves(self, k):
        current_x, current_y = 0, 0

        for _ in range(k+1):
            legal_moves = self.get_legal_moves(current_x, current_y)

            if not legal_moves:
                break

            next_move = random.choice(legal_moves)
            current_x, current_y = next_move

            self.visited += 1
            self.board[current_x][current_y] = self.visited

        return current_x, current_y 


    def backtrack_dfs(self, x, y,p):
        stack = [(x, y)] # I initialized the stack with the starting position this position is the last position of the k moves
        visited_count = 1 #only one square is visited at the beginning

        while stack:
            current_x, current_y = stack[-1]
            legal_moves = self.get_legal_moves(current_x, current_y)

            if not legal_moves:
                # No legal moves from the current position, backtrack
                self.visited -= 1
                self.board[current_x][current_y] = -1

                #visited_count -= 1 # Update the number of visited squares
                stack.pop()

            else:
                # Choose the next move and update the board
                next_move = legal_moves.pop()
                next_x, next_y = next_move
                stack.append((next_x, next_y)) # Push the next move to the stack
                self.visited += 1 # Update the number of visited squares
                self.board[next_x][next_y] = self.visited # Update the board kaçıncı adımda olduğunu gösteriyor
                visited_count += 1 # Update the number of visited squares

                # Check if the tour is complete
                #print("visited count is: ",visited_count)
                #print("p*n*n is: ",p*self.n * self.n)
                if visited_count > p*self.n * self.n:  #if the number of visited squares is greater than p*n*n then the tour is 
                    #succesfully completed
                    return True

        return False

n = 8  #size 
#measure the time of each algorithm

knights_tour = KnightsTour(n) 

time_elapsed(knights_tour.las_vegas_algorithm, p=0.7, k=0)


time_elapsed(knights_tour.las_vegas_algorithm, p=0.7, k=2)

time_elapsed(knights_tour.las_vegas_algorithm, p=0.7, k=3)

time_elapsed(knights_tour.las_vegas_algorithm, p=0.8, k=0)


time_elapsed(knights_tour.las_vegas_algorithm, p=0.8, k=2)

time_elapsed(knights_tour.las_vegas_algorithm, p=0.8, k=3)

time_elapsed(knights_tour.las_vegas_algorithm, p=0.85, k=0)

time_elapsed(knights_tour.las_vegas_algorithm, p=0.85, k=2)

time_elapsed(knights_tour.las_vegas_algorithm, p=0.85, k=3)