import sudoku
import time


def write_board(board, filename):
    """Write board to a file

    Parameters
    ----------
        board : list[list[int]]

        filename : str
    """

    filename = __file__.replace("file_operations.py", f"{filename}.txt")

    dashes = ("-" * 9).join([" "] * 4) * 3 + "\n"
    bars = (" " * 9).join(["|"] * 4) * 3 + "\n"

    with open(filename, "w") as f:
        for i in range(9):
            f.write(dashes)
            f.write(bars)
            f.write(bars)
            for j in range(9):
                f.write("|")
                if j == 3 or j == 6:
                    f.write("|")
                if board[i][j] != 0:
                    f.write(f"    {board[i][j]}    ")
                else:
                    f.write("         ")
            f.write("|\n")
            f.write(bars)
            f.write(bars)
            f.write(dashes)
            if i == 2 or i == 5:
                f.write(dashes)
        f.write(dashes + "\n\n")

    print(filename)


def main():
    # generate complete board
    solution = sudoku.generate_board()

    # copy orignal board and make empty cells
    board = [i.copy() for i in solution]
    board = sudoku.remove_fields(board)

    # generate puzzle board and write in file
    print("Sudoku game is written in:")
    write_board(board, 'sudoku_game')
    print("\nYou can play sudoku game now")

    start_time = time.time()
    choose = input("If you finish game enter (y or yes): ").strip().lower()
    if choose == 'y' or choose == 'yes':
        end_time = time.time()
        time_taken = end_time - start_time
        print(
            f"Time taken: {time_taken // 60:.0f} minutes {time_taken%60:.0f} Seconds ")

    # ask users to save original solution
    ans = input("Do you need to show solution(y or yes): ").strip().lower()
    if ans == 'y' or ans == 'yes':
        print("Solution file is written to:")
        write_board(solution, 'solution')


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGood Bye! 👋")
        exit()
