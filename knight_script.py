import sys
import subprocess

def run_part1():
    subprocess.run(["python3", "part1.py"])

def run_part2():
    subprocess.run(["python3", "part2.py"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_script.py <part1 or part2>")
        sys.exit(1)

    option = sys.argv[1]

    if option == "part1":
        run_part1()
    elif option == "part2":
        run_part2()
    else:
        print("Invalid argument. Use 'part1' or 'part2'.")
        sys.exit(1)
