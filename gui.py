# Milosoiu Andrei
# Email: andrei18.milosoiu@gmail.com

import os
import subprocess
import select
import tkinter as tk
from tkinter import *
from tkinter import ttk

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

	subprocess.call(['python3', cmd_script, cmd_song_cnt, cmd_term])

def display(x):
	selection = x

# Main
root = tk.Tk(
	screenName=None,
	baseName=None,
	className='Tk',
	useTk=1
)
root.title("TrebleTop")
root.geometry("500x300")

# TrebleTop Name
label = ttk.Label(
	root,
	text="TrebleTop"
)
label.pack()

# Spinbox
# 1. Spinbox Label
label = ttk.Label(
	root,
	text="Number of songs in the playlist:"
)
label.pack()

# 2. Spinbox Body
curr_song_cnt = tk.StringVar(value=100)
song_cnt = ttk.Spinbox(
	root,
	from_=50,
	to=1000,
	increment = 50,
	command=display(curr_song_cnt.get()),
	textvariable=curr_song_cnt
)

song_cnt.config(width=30)

song_cnt.pack(
	padx=20,
	pady=20
)

# Combobox
# 1. Combobox Label
label = ttk.Label(
	root,
	text="Time interval:")
label.pack()

# 2. Combobox Body
curr_term = tk.StringVar(value=100)
term = ttk.Combobox(
	root,
	values=["Last month", "Last 6 months", "All time"],
	state="readonly",
	textvariable=curr_term
)
term.pack(pady=5)
term.set("Last month")
term.bind(
	"<<ComboboxSelected>>",
	display
)
term.config(
	justify="center",
	width=30
)

# Update Button
update_button = ttk.Button(
	root,
	text="Update Playlist",
	width=25,
	command=click_update_button
)
update_button.pack(
	padx=20,
	pady=20
)

root.mainloop()