import math
import random


def is_valid_move(x, y, visited):
    return 0 <= x < 8 and 0 <= y < 8 and visited[x][y] == -1


def get_possible_moves(x, y, visited):
    moves = [
        (x + 1, y + 2), (x + 2, y + 1),
        (x + 2, y - 1), (x + 1, y - 2),
        (x - 1, y - 2), (x - 2, y - 1),
        (x - 2, y + 1), (x - 1, y + 2)
    ]
    return [(a, b) for a, b in moves if is_valid_move(a, b, visited)]


def knight_tour(p):
    board_size = 8
    total_squares = board_size * board_size
    target_squares = math.ceil(total_squares * p)
    success_count = 0

    with open(f"results_{p}.txt", "w") as file:
        for run in range(1, 100001):
            # Initialize the chessboard and the starting position
            chessboard = [[-1] * board_size for _ in range(board_size)]
            current_x, current_y = random.randint(0, 7), random.randint(0, 7)
            chessboard[current_y][current_x] = 0
            visited_squares = 1
            file.write(f"Run {run}: starting from ({current_x},{current_y})\n")

            while visited_squares < target_squares:
                possible_moves = get_possible_moves(current_x, current_y, chessboard)
                if not possible_moves:
                    #################
                    break  # Dead end

                next_x, next_y = random.choice(possible_moves)
                chessboard[next_y][next_x] = visited_squares
                current_x, current_y = next_x, next_y
                visited_squares += 1

                # Write the tour steps to file inside the loop
                file.write(f"Stepping into ({next_y},{next_x})\n")

            if visited_squares >= target_squares:
                success_count += 1

            # Write the result of the run to file outside the loop
            result = "Successful" if visited_squares >= target_squares else "Unsuccessful"
            file.write(f"{result} - Tour length: {visited_squares}\n")

            # Write the sequence of squares stepped on to file outside the loop
            for row in chessboard:
                file.write(" ".join(str(square) for square in row) + "\n")

# Print the overall statistics
    probability = success_count / 100000
    print(f"LasVegas Algorithm With p = {p}")
    print(f"Number of successful tours: {success_count}")
    print(f"Number of trials: 100000")
    print(f"Probability of a successful tour: {probability}")


if __name__ == "__main__":
    success_percentages = [0.7, 0.8, 0.85]

    for p in success_percentages:
        knight_tour(p)
