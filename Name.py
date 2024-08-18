import turtle
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import svgutils.transform as st
from svg_turtle import SvgTurtle
import os


def draw_turtle_part(file_path):
    # draw a circle with solid color
    t = SvgTurtle(100, 100)
    t.up()
    t.goto(0, -50)
    t.down()
    t.begin_fill()
    t.fillcolor('red')
    t.circle(40)
    t.end_fill()

    # save it as a svg file
    t.save_as(file_path)
    return


def draw_opacity_part(file_path):
    # draw a triangle with a color of 50% opacity

    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
    ax.set_xlim(-50, 50)  # set the canvas size scale the same as turtle
    ax.set_ylim(-50, 50)  # set the canvas size scale the same as turtle
    ax.axis('off')  # hide the axis

    # draw and fill a triangle with an RGBA color
    polygon = patches.Polygon(
        [(-50, 0), (0, 50), (50, 0), (-50, 0)],
        closed=True, linewidth=0, fill=True, color=(0, 0.8, 0, 0.5))
    ax.add_patch(polygon)

    # save the figure, remove the paddings and white space surrounding the plot
    plt.savefig(file_path, format='svg', transparent=True, bbox_inches='tight', pad_inches=0)
    return


def combine_two_parts(file_1, file_2):
    x, y = 100, 100
    fig1 = st.fromfile(file_1)

    # resize the figure to make sure the two align
    fig1.set_size((f'{x}pt', f'{y}pt'))
    fig2 = st.fromfile(file_2)

    # resize the figure to make sure the two align
    fig2.set_size((f'{x}px', f'{y}px'))
    fig1.append(fig2)
    fig1.save('result.svg')


if __name__ == '__main__':
    draw_turtle_part('test1.svg')
    draw_opacity_part('test2.svg')
    combine_two_parts('test1.svg', 'test2.svg')
    os.remove('test1.svg')  # optional
    os.remove('test2.svg')  # optional