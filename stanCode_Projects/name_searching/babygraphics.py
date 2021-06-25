"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    basic_x = (width - GRAPH_MARGIN_SIZE) / len(YEARS)
    x_coordinate = year_index * basic_x + GRAPH_MARGIN_SIZE

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # the top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, width=LINE_WIDTH,
                       fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                       , width=LINE_WIDTH, fill='black')

    # the bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH, fill='black')
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT,
                       width=LINE_WIDTH, fill='black')

    # draw line by year
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill='black')
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW, font='times 10')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # to calculate the y distance by each rank (within 1000)
    get_y = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/MAX_RANK
    for lookup in lookup_names:
        # color difference by each name
        color_number = lookup_names.index(lookup) % 4
        color = COLORS[color_number]
        if lookup in name_data:
            if str(YEARS[0]) in name_data[lookup] and int(name_data[lookup][str(YEARS[0])]) <= 1000:
                point1_x = get_x_coordinate(CANVAS_WIDTH, 0)
                point1_y = GRAPH_MARGIN_SIZE + int(name_data[lookup][str(YEARS[0])]) * get_y
                canvas.create_text(point1_x + TEXT_DX, point1_y-GRAPH_MARGIN_SIZE, text=lookup + ' ' +
                                   name_data[lookup][str(YEARS[0])],
                                   anchor=tkinter.NW, font='times 10', fill=color)
            else:
                # if the rank over 1000 or not exist.
                point1_x = get_x_coordinate(CANVAS_WIDTH, 0)
                point1_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(point1_x + TEXT_DX, point1_y - GRAPH_MARGIN_SIZE, text=lookup + '*',
                                   anchor=tkinter.NW, font='times 10', fill=color)

            for i in range(1, len(YEARS)):
                if str(YEARS[i]) in name_data[lookup] and int(name_data[lookup][str(YEARS[i])]) <= 1000:
                    point2_x = get_x_coordinate(CANVAS_WIDTH, i)
                    point2_y = GRAPH_MARGIN_SIZE + int(name_data[lookup][str(YEARS[i])]) * get_y
                    canvas.create_line(point1_x, point1_y, point2_x, point2_y, width=LINE_WIDTH, fill=color)
                    canvas.create_text(point2_x + TEXT_DX, point2_y-GRAPH_MARGIN_SIZE, text=lookup+' ' +
                                       name_data[lookup][str(YEARS[i])],
                                       anchor=tkinter.NW, font='times 10', fill=color)
                else:
                    # if the rank over 1000 or not exist.
                    point2_x = get_x_coordinate(CANVAS_WIDTH, i)
                    point2_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    canvas.create_line(point1_x, point1_y, point2_x, point2_y, width=LINE_WIDTH, fill=color)
                    canvas.create_text(point2_x + TEXT_DX, point2_y-GRAPH_MARGIN_SIZE, text=lookup+'*',
                                       anchor=tkinter.NW, font='times 10', fill=color)

                # change the point2 to next year's point1
                point1_x = point2_x
                point1_y = point2_y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
