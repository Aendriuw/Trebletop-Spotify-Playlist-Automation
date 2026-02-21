# Milosoiu Andrei
# Email: andrei18.milosoiu@gmail.com

import os
import subprocess
import select
import tkinter as tk
from tkinter import *
from tkinter import ttk

def click_update_button():
	command1 = "spotify-script.py"
	cmd_song_cnt = current_value.get()
	cmd_term = "short_term"

	subprocess.call(['python3', command1, cmd_song_cnt, cmd_term])

def display():
	selection = song_cnt.get()

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title("TrebleTop")
root.geometry("500x300")

# TrebleTop Name
label = ttk.Label(root, text="TrebleTop")
label.pack()

# Spinbox
# 1. Spinbox Label
label = ttk.Label(root, text="How many songs in the playlist?")
label.pack()

# 2. Spinbox Body
current_value = tk.StringVar(value=100)
song_cnt = ttk.Spinbox(
	root,
	from_=50,
	to=1000,
	increment = 50,
	command=display,
	textvariable=current_value)

song_cnt.config(
	width=30)

song_cnt.pack(padx=20, pady=20)

# Combobox: term
term = ttk.Combobox(
    root,
    values=["short_term", "medium_term", "long_term"],
    state="readonly"
)
term.pack(pady=5)
term.set("short_term")
term.bind("<<ComboboxSelected>>", select)
term.config(justify="center", width=30)

# Update Button
update_button = ttk.Button(root, text="Update Playlist", width=25, command=click_update_button)
update_button.pack()

root.mainloop()