# Milosoiu Andrei
# Email: andrei18.milosoiu@gmail.com

import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

# Functions
def click_update_button():
	cmd_script = "spotify-script.py"
	cmd_song_cnt = curr_song_cnt.get()
	aux_term = curr_term.get()
	cmd_term = "short_term"

	if aux_term == "Last 6 months":
		cmd_term = "medium_term"
	elif aux_term == "All time":
		cmd_term = "long_term"

	if int(curr_song_cnt.get()) % 50 != 0:
		tkinter.messagebox.showerror("Error", "Please enter a multiple of 50.\n( e.g. 50, 100, 150 ... )")
	else:
		try:
			subprocess.call(['python3', cmd_script, cmd_song_cnt, cmd_term])
			tkinter.messagebox.showinfo("Information", "Your playlist has been modified successfully.")
		except:
			tkinter.messagebox.showerror("Error", "An error occurred. Check README for possible issues.")

def display(x):
	selection = x

# Main
# Window
root = tk.Tk()
root.title("TrebleTop")

# Theme
root.tk.call(
	"source",
	"azure.tcl"
)
root.tk.call(
	"set_theme",
	"dark"
)

# Outer padding frame
outer = ttk.Frame(root)
outer.pack(
	fill="both",
	expand=True,
	padx=20,
	pady=20
)

# Header
header = ttk.Frame(outer)
header.pack(
	fill="x",
	pady=(0, 4)
)

# Trebletop Name
label = ttk.Label(
	header,
	text="TrebleTop",
	font=("Helvetica", 22, "bold")
)
label.pack()

# Settings settings_frame
settings_frame = ttk.LabelFrame(
	outer,
	text="Settings",
	padding=(16, 12)
)
settings_frame.pack(fill="x")

# Spinbox (Song count)
# 1. Spinbox Label
song_label = ttk.Label(
	settings_frame,
	text="Number of songs (multiples of 50)",
	font=("Helvetica", 10)
)
song_label.pack(anchor="w")

# 2. Spinbox Body
curr_song_cnt = tk.StringVar(value=100)
song_cnt = ttk.Spinbox(
    settings_frame,
    from_=50,
	to=1000,
	increment=50,
    command=display(curr_song_cnt.get()),
    textvariable=curr_song_cnt,
    width=32
)

song_cnt.pack(
	pady=(4, 14),
	fill="x"
)

# Separator
separator = ttk.Separator(
	settings_frame,
	orient="horizontal"
)
separator.pack(
	fill="x",
	pady=(0, 14)
)

# Combobox (time range)
# 1. Combobox Label
term_label = ttk.Label(
	settings_frame,
	text="Time range",
	font=("Helvetica", 10)
)
term_label.pack(anchor="w")

# 2. Combobox Body
curr_term = tk.StringVar()
term = ttk.Combobox(
    settings_frame,
    values=["Last month", "Last 6 months", "All time"],
    state="readonly",
    textvariable=curr_term,
    width=32
)
term.set("Last month")
term.bind(
	"<<ComboboxSelected>>",
	display
)
term.config(justify="center")
term.pack(
	pady=(4, 0),
	fill="x"
)

# Update button
update_button = ttk.Button(
	root,
	text="Update Playlist",
	width=28,
	command=click_update_button,
	style="Accent.TButton"
)
update_button.pack(pady=(0, 18))

# Window size
root.update()
x_cordinate = int(5 * root.winfo_screenwidth()  / 12)
y_cordinate = int(3 * root.winfo_screenheight() / 10)
root.geometry(f"+{x_cordinate}+{y_cordinate}")
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
