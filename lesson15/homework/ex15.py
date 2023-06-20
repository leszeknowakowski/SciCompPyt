import tkinter as tk
import random
import os
import matplotlib
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use('TkAgg')

root = tk.Tk()

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT)

'''create a list of png images to view'''
directory = 'png'
images = []
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        img = tk.PhotoImage(file=os.path.join(directory, filename))
        images.append(img)

results = []


def result_print():
    """"add a canvas with appropriate dice image if empty and stores results in list"""
    rolling_result = random.randint(1, 6)
    results.append(rolling_result)
    if 'img' not in locals() and 'img' not in globals():
        img = dice_canvas.create_image(20, 20,  anchor=tk.NW, image=images[rolling_result-1])
    else:  # if not empty delete previous canvas and make new one with new image
        dice_canvas.delete('all')
        img = dice_canvas.create_image(20, 20, anchor=tk.NW, image=images[rolling_result - 1])
    return img


def create_plot():
    """creates canvas and adds a plot of results"""
    fig = Figure(figsize=(4, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(range(1, len(results) + 1), results)
    plot.set_xlabel("Roll Number")
    plot.set_ylabel("Dice Result")

    global plot_canvas
    plot_canvas = FigureCanvasTkAgg(fig, master=root)
    plot_canvas.draw()
    plot_canvas.get_tk_widget().pack()


def show_plot():
    """shows a plot of results so far"""
    if len(results) == 0:  # checks if there were any rolls yet
        tk.messagebox.showwarning("No Results", "No dice roll results available.")
    else:
        if 'plot_canvas' not in globals():
            create_plot()
            toolbar = NavigationToolbar2Tk(plot_canvas, root)
            toolbar.update()
        else:  # if canvas already exists
            plot_canvas.get_tk_widget().destroy()
            create_plot()


def print_median():
    if len(results) == 0:
        tk.messagebox.showwarning("No Results", "No dice roll results available.")
    else:
        median = np.median(results)
        median_label.config(text="median: {}".format(median))
        median_label.pack()


def print_average():
    if len(results) == 0:
        tk.messagebox.showwarning("No Results!", "No dice roll results available")
    else:
        avg = np.mean(results)
        avg_label.config(text='mean: {}'.format(avg))
        avg_label.pack()


canvas_width, canvas_height = 150, 150
dice_canvas = tk.Canvas(right_frame, width=canvas_width, height=canvas_height)
dice_canvas.pack()


# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "Print" menu
print_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Print", menu=print_menu)

# Add a command to print the median and average of dice roll results
print_menu.add_command(label="Median", command=print_median)
print_menu.add_command(label="average", command=print_average)

median_label = tk.Label(right_frame, text="Median: -")
avg_label = tk.Label(right_frame, text="Average: -")

roll_button = tk.Button(right_frame, text = "roll a dice", width=45, height=5, bg="#6cb9a2", command=result_print)
roll_button.pack()

show_plot_button = tk.Button(right_frame, text="show plot", width=45, height=5, command=show_plot)
show_plot_button.pack()

root.mainloop()
