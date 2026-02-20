# Milosoiu Andrei
# Email: andrei18.milosoiu@gmail.com

import tkinter as tk
import os

def click_update_button():
	os.system("python spotify-script.py 100 short_term")

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

label = tk.Label(root, text="TrebleTop")
label.pack()

update_button = tk.Button(root, text="Update Playlist", width=25, command=click_update_button)
update_button.pack()

root.mainloop()