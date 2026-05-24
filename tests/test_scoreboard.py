import sys
from pathlib import Path

# Добавляем папку src в путь импорта, чтобы тесты видели модуль scoreboard.py
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from scoreboard import can_display_poster, can_show_color


def test_black_color() -> None:
    """Черный цвет должна отображать любая ячейка табло."""

    for code in range(8):
        assert can_show_color(".", code) is True


def test_red_color() -> None:
    """Красный цвет должны отображать только коды 4, 5, 6, 7."""

    for code in range(8):
        expected = code in [4, 5, 6, 7]
        assert can_show_color("R", code) == expected


def test_green_color() -> None:
    """Зеленый цвет должны отображать только коды 2, 3, 6, 7."""

    for code in range(8):
        expected = code in [2, 3, 6, 7]
        assert can_show_color("G", code) == expected


def test_blue_color() -> None:
    """Синий цвет должны отображать только коды 1, 3, 5, 7."""

    for code in range(8):
        expected = code in [1, 3, 5, 7]
        assert can_show_color("B", code) == expected


def test_example_with_no_answer() -> None:
    """Первый пример из задания должен вернуть False."""

    poster = [
        ".GB",
        "R.B",
        "RG.",
    ]

    board = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 0],
    ]

    assert can_display_poster(poster, board) is False


def test_example_with_yes_answer() -> None:
    """Второй пример из задания должен вернуть True."""

    poster = [
        "RGB",
        ".G.",
    ]

    board = [
        [7, 7, 7],
        [7, 7, 7],
    ]

    assert can_display_poster(poster, board) is True


def test_one_cell_success() -> None:
    """Проверка случая 1 на 1, когда цвет можно показать."""

    poster = ["R"]
    board = [[4]]

    assert can_display_poster(poster, board) is True


def test_one_cell_fail() -> None:
    """Проверка случая 1 на 1, когда цвет нельзя показать."""

    poster = ["R"]
    board = [[2]]

    assert can_display_poster(poster, board) is False


def run_tests() -> None:
    """Запускает все тесты."""

    test_black_color()
    test_red_color()
    test_green_color()
    test_blue_color()
    test_example_with_no_answer()
    test_example_with_yes_answer()
    test_one_cell_success()
    test_one_cell_fail()

    print("All tests passed")


if __name__ == "__main__":
    run_tests()