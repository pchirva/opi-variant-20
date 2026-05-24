def can_show_color(color: str, capability: int) -> bool:
    """
    Проверяет, может ли ячейка табло показать нужный цвет.

    color:
    R - красный
    G - зеленый
    B - синий
    . - черный

    capability:
    число от 0 до 7, описывающее возможности ячейки табло.
    """

    # Черный цвет может показать любая ячейка
    if color == ".":
        return True

    # Списки кодов, которые поддерживают каждый цвет
    red_codes = [4, 5, 6, 7]
    green_codes = [2, 3, 6, 7]
    blue_codes = [1, 3, 5, 7]

    if color == "R":
        return capability in red_codes

    if color == "G":
        return capability in green_codes

    if color == "B":
        return capability in blue_codes

    return False


def can_display_poster(poster: list[str], board: list[list[int]]) -> bool:
    """
    Проверяет, можно ли отобразить всю рекламную заставку на табло.

    poster - список строк с цветами заставки.
    board - матрица возможностей ячеек табло.
    """

    for i in range(len(poster)):
        for j in range(len(poster[i])):
            color = poster[i][j]
            capability = board[i][j]

            # Если хотя бы одну клетку нельзя отобразить, сразу возвращаем False
            if not can_show_color(color, capability):
                return False

    return True
