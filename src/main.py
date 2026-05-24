from scoreboard import can_display_poster


def read_input() -> tuple[list[str], list[list[int]]]:
    """
    Считывает входные данные:
    n, m
    n строк заставки
    n строк возможностей табло
    """

    n, m = map(int, input().split())

    poster = []

    for _ in range(n):
        poster.append(input().strip())

    board = []

    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)

    return poster, board


def main() -> None:
    poster, board = read_input()

    if can_display_poster(poster, board):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()