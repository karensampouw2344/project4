from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

if __name__ == "__main__":
    # Generate and show line plot
    line_fig = draw_line_plot()
    line_fig.show()

    # Generate and show bar plot
    bar_fig = draw_bar_plot()
    bar_fig.show()

    # Generate and show box plot
    box_fig = draw_box_plot()
    box_fig.show()
