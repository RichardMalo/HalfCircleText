import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import random
import matplotlib.colors as mcolors

class SentenceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Half Circle Art")
        
        self.bg_color = 'black'
        self.txt_color = 'white'
        self.line_color = 'white'
        self.font_size = 10
        self.font_style = 'normal'
        
        self.create_widgets()

    def create_widgets(self):
        self.create_menu()
        self.create_entry()
        self.create_font_size_selector()
        self.create_font_style_selector()
        self.create_color_picker("Select Background Color", 'black', lambda val: setattr(self, 'bg_color', val))
        self.create_color_picker("Select Text Color", 'white', lambda val: setattr(self, 'txt_color', val))
        self.create_color_picker("Select Line Color", 'white', lambda val: setattr(self, 'line_color', val))
        self.create_capitalize_option()
        self.create_buttons()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.clear_entry)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Clear", command=self.clear_entry)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menubar)

    def create_entry(self):
        tk.Label(self.root, text="Enter a new sentence:").pack()
        self.sentence_entry = tk.Entry(self.root, width=60)
        self.sentence_entry.insert(0, "a year from now you will wish you started today")
        self.sentence_entry.pack()
        tk.Button(self.root, text="Clear", command=self.clear_entry).pack()

    def create_font_size_selector(self):
        tk.Label(self.root, text="Select Font Size:").pack()
        font_size_var = tk.StringVar(self.root)
        font_size_var.set(str(self.font_size))
        
        font_sizes = ["8","9","10","11","12","14","16","18","20","22","24","26","28","36","48","72"]
        font_size_option = ttk.Combobox(self.root, textvariable=font_size_var, values=font_sizes, width=58)
        font_size_option.bind("<<ComboboxSelected>>", lambda event: setattr(self, 'font_size', int(font_size_var.get())))
        font_size_option.pack()

    def create_font_style_selector(self):
        tk.Label(self.root, text="Select Font Style:").pack()
        font_style_var = tk.StringVar(self.root)
        font_style_var.set(self.font_style)
        
        font_styles = ["normal", "bold", "italic", "oblique"]
        font_style_option = ttk.Combobox(self.root, textvariable=font_style_var, values=font_styles, width=58)
        font_style_option.bind("<<ComboboxSelected>>", lambda event: setattr(self, 'font_style', font_style_var.get()))
        font_style_option.pack()

    def create_color_picker(self, label, default_color, callback):
        tk.Label(self.root, text=label).pack()
        color_var = tk.StringVar(self.root)
        color_var.set(default_color)
        color_option = ttk.Combobox(self.root, textvariable=color_var, values=self.get_color_list(), width=58)
        color_option.bind("<<ComboboxSelected>>", lambda event: callback(color_var.get()))
        color_option.pack()

    def create_capitalize_option(self):
        self.var_capitalize = tk.BooleanVar()
        self.var_capitalize.set(False)
        tk.Label(self.root, text="Capitalize first letter of each word").pack()
        tk.Checkbutton(self.root, variable=self.var_capitalize).pack()

        # Added lines for ALL CAPS option
        self.var_all_caps = tk.BooleanVar()
        self.var_all_caps.set(False)
        tk.Label(self.root, text="Convert sentence to ALL CAPS").pack()
        tk.Checkbutton(self.root, variable=self.var_all_caps).pack()

    def create_buttons(self):
        tk.Button(self.root, text="Preview", command=self.preview).pack()
        tk.Button(self.root, text="Submit", command=self.submit).pack()
        tk.Button(self.root, text="Random 20 Save", command=self.save_random_20).pack()

    def get_color_list(self):
        preferred_colors = ['black', 'white', 'red', 'blue', 'green', 'yellow', 'purple', 'aqua', 'magenta']
        all_colors = [color for color in mcolors.CSS4_COLORS.keys() if color not in preferred_colors]
        return preferred_colors + all_colors

    def clear_entry(self):
        self.sentence_entry.delete(0, 'end')

    def create_sentence_plot(self, sentence=None, bg_color=None, txt_color=None, line_color=None, capitalize=False):
        if not sentence:
            sentence = self.sentence_entry.get()
        if self.var_all_caps.get():
            sentence = sentence.upper()
        elif capitalize or self.var_capitalize.get():
            sentence = sentence.title()
        words = sentence.split()

        fig, ax = plt.subplots(figsize=(10, 10))
        fig.patch.set_facecolor(bg_color or self.bg_color)
        ax.set_facecolor(bg_color or self.bg_color)
        ax.set_aspect('equal')

        n = len(words)
        x = np.linspace(0, 2*n, n)
        y = [0] * n
        radius = abs(x[-2] - x[0]) / 2

        for i in range(n-1):
            # Check if font_style is 'bold'
            if self.font_style == 'bold':
                ax.text(x[i], y[i], words[i], color=txt_color or self.txt_color, ha='center', fontsize=self.font_size, fontweight='bold')
            else:
                ax.text(x[i], y[i], words[i], color=txt_color or self.txt_color, ha='center', fontsize=self.font_size, style=self.font_style)
        ax.text(radius, -radius - 1, words[-1], color=txt_color or self.txt_color, ha='center', fontsize=self.font_size, style=self.font_style if self.font_style != 'bold' else None, fontweight='bold' if self.font_style == 'bold' else None)


        for i in range(1, n-1):
            radius_i = abs(x[i] - x[0]) / 2
            arc = Arc((radius_i, 0.6), 2*radius_i, 2*radius_i, theta1=0, theta2=180, edgecolor=line_color or self.line_color, lw=2)
            ax.add_patch(arc)

        start_arc_1, end_arc_1 = 180, 270
        start_arc_2, end_arc_2 = 270, 360

        arc_1 = Arc((radius, -0.25), 2*radius, 2*radius, theta1=start_arc_1, theta2=end_arc_1, edgecolor=bg_color or self.bg_color, lw=2)
        arc_2 = Arc((radius, -0.25), 2*radius, 2*radius, theta1=start_arc_2, theta2=end_arc_2, edgecolor=line_color or self.line_color, lw=2)

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
            fig.savefig(file_path, dpi=1200, format='png')

    def save_random_20(self):
        if not os.path.exists("Random"):
            os.mkdir("Random")

        for i in range(20):
            random_bg_color = random.choice(self.get_color_list())
            random_txt_color = random.choice(self.get_color_list())
            random_line_color = random.choice(self.get_color_list())

            fig = self.create_sentence_plot(bg_color=random_bg_color, txt_color=random_txt_color, line_color=random_line_color)
            filename = f"Random/random_combination_{i + 1}.jpg"
            fig.savefig(filename, dpi=600, format="png")
            
            # Close the figure after saving
            plt.close(fig)

if __name__ == "__main__":
    root = tk.Tk()
    app = SentenceApp(root)
    root.mainloop()