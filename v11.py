import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.colors as mcolors

class SentenceApp:
    def __init__(self, root):
        self.bg_color = 'black'
        self.txt_color = 'white'
        self.line_color = 'white'
        self.root = root
        self.root.title("Half Circle Art")
        self.create_widgets()

    def create_widgets(self):
        self.create_entry_widgets()
        self.create_color_picker("Select Background Color", 'black', lambda val: setattr(self, 'bg_color', val))
        self.create_color_picker("Select Text Color", 'white', lambda val: setattr(self, 'txt_color', val))
        self.create_color_picker("Select Line Color", 'white', lambda val: setattr(self, 'line_color', val))
        self.create_capitalize_checkbox()
        self.create_buttons()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # Create a File menu with two options
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Create an Edit menu with one option for this example
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Clear", command=self.clear_entry)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Display the menu
        self.root.config(menu=menubar)

    def new_file(self):
        # For demonstration, let's just clear the entry when "New" is selected
        self.clear_entry()

    def create_entry_widgets(self):
        tk.Label(self.root, text="Enter a sentence:").pack()
        self.entry = tk.Entry(self.root, width=60)
        self.entry.insert(0, "a year from now you will wish you started today")
        self.entry.pack()
        tk.Button(self.root, text="Clear", command=self.clear_entry).pack()

    def create_color_picker(self, text, default, callback):
        tk.Label(self.root, text=text).pack()
        color_var = tk.StringVar(self.root, value=default)
        color_option = ttk.Combobox(self.root, textvariable=color_var, values=self.get_color_list(), width=58)
        color_option.pack()
        color_var.trace_add('write', lambda *args: callback(color_var.get()))

    def create_capitalize_checkbox(self):
        self.capitalize_var = tk.BooleanVar(value=False)
        tk.Label(self.root, text="Capitalize first letter of each word").pack()
        tk.Checkbutton(self.root, variable=self.capitalize_var).pack()

    def create_buttons(self):
        tk.Button(self.root, text="Preview", command=self.preview).pack()
        tk.Button(self.root, text="Submit", command=self.submit).pack()

    def clear_entry(self):
        self.entry.delete(0, 'end')

    def get_color_list(self):
        # Specified colors that should appear first
        preferred_colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'purple', 'aqua', 'magenta']
        
        # Get all colors from CSS4_COLORS and remove the preferred ones to avoid duplicates
        all_colors = [color for color in mcolors.CSS4_COLORS.keys() if color not in preferred_colors]
        
        # Combine lists: preferred colors first, then the rest
        return preferred_colors + all_colors

    def create_sentence_plot(self):
        sentence = self.entry.get()
        if self.capitalize_var.get():
            sentence = sentence.title()
        words = sentence.split()

        fig, ax = plt.subplots(figsize=(10, 10))
        fig.patch.set_facecolor(self.bg_color)
        ax.set_facecolor(self.bg_color)
        ax.set_aspect('equal')
        n = len(words)
        x = np.linspace(0, 2*n, n)
        y = [0] * n
        radius = abs(x[-2] - x[0]) / 2
        
        for i in range(n-1):
            ax.text(x[i], y[i], words[i], color=self.txt_color, ha='center')

        ax.text(radius, -radius - 1, words[-1], color=self.txt_color, ha='center')
        for i in range(1, n-1):
            radius_i = abs(x[i] - x[0]) / 2
            arc = Arc((radius_i, 0.5), 2*radius_i, 2*radius_i,
                      theta1=0, theta2=180, edgecolor=self.line_color, lw=2)
            ax.add_patch(arc)

        start_arc_1, end_arc_1 = 180, 270
        start_arc_2, end_arc_2 = 270, 360

        arc_1 = Arc((radius, -0.25), 2*radius, 2*radius,
                    theta1=start_arc_1, theta2=end_arc_1, edgecolor=self.bg_color, lw=2)
        arc_2 = Arc((radius, -0.25), 2*radius, 2*radius,
                    theta1=start_arc_2, theta2=end_arc_2, edgecolor=self.line_color, lw=2)

        ax.add_patch(arc_1)
        ax.add_patch(arc_2)

        ax.axis('off')
        ax.set_xlim(-1, 2*n+1)
        ax.set_ylim(-radius-2, radius+2)

        return fig

    def preview(self):
        fig = self.create_sentence_plot()

        def on_plot_closing():
            self.root.deiconify()
            new_root.destroy()

        self.root.iconify()
        new_root = tk.Toplevel(self.root)
        new_root.state('zoomed')
        canvas = FigureCanvasTkAgg(fig, master=new_root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button = tk.Button(master=new_root, text="Save Image", command=lambda: self.save_image(fig))
        button.pack(side=tk.BOTTOM)
        new_root.protocol("WM_DELETE_WINDOW", on_plot_closing)

    def submit(self):
        fig = self.create_sentence_plot()
        self.save_image(fig)

    def save_image(self, fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", initialdir=".")
        if file_path:
            fig.savefig(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = SentenceApp(root)
    root.mainloop()