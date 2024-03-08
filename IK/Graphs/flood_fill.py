"""
Author: Soumil Ramesh Kulkarni
Date: 03.06.2024

Question:
One pixel on a grayscale image changes color. Recolor all the adjacent pixels of the same color to the same new color.

Grayscale colors are simply numbers.

Example One
{
"pixel_row": 0,
"pixel_column": 1,
"new_color": 2,
"image": [
[0, 1, 3],
[1, 1, 1],
[1, 5, 4]
]
}
I.e. the pixel at row 0 and column 1 changes to color 2.

Output:

[
[0, 2, 3],
[2, 2, 2],
[2, 5, 4]
]
Example Two
{
"pixel_row": 1,
"pixel_column": 0,
"new_color": 9,
"image": [
[0, 2, 1],
[1, 1, 2],
[2, 5, 4]
]
}
I.e. the pixel at row 1 and column 0 changes to color 9.

Output:

[
[0, 2, 1],
[9, 9, 2],
[2, 5, 4]
]
"""


def flood_fill(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # USE BFS to fill up new colors

    if image[pixel_row][pixel_column] == new_color:
        return image

    old_color = image[pixel_row][pixel_column]
    image[pixel_row][pixel_column] = new_color

    queue = [(pixel_row, pixel_column)]
    directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    while queue:
        row, column = queue.pop(0)

        for dx, dy in directions:
            new_row = row + dx
            new_column = column + dy

            if 0 <= new_row < len(image) and 0 <= new_column < len(image[0]) and image[new_row][
                new_column] == old_color:
                image[new_row][new_column] = new_color
                queue.append((new_row, new_column))
    return image