#!/usr/bin/env python3
from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import platform
import os
import sys
import tkinter.font as tkfont

if platform.system()=='Windows':
	import pyglet
	pyglet.options['win32_gdi_font'] = True
	fontpath1 = Path(__file__).parent / 'usrfont1'
	pyglet.font.add_file(str(fontpath1))
	fontpath2 = Path(__file__).parent / 'usrfont2'
	pyglet.font.add_file(str(fontpath2))
	
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()
root.title('Currency Conversion')

conv_btn = PhotoImage(file=resource_path("button_convert.png"))
lock_btn = PhotoImage(file=resource_path("button_lock.png"))
unlock_btn = PhotoImage(file=resource_path("button_unlock.png"))
clear_btn = PhotoImage(file=resource_path("button_clear.png"))

s = ttk.Style()
s.theme_create('pastel', settings={
	".": {
		"configure": {
			"background": '#eab676',  # All except tabs
			"font": 'black'
		}
	},
	"TNotebook": {
		"configure": {
			"background": '#ba7330',  # Your margin color
			"tabmargins": [0, 0, 0, 0],  # margins: left, top, right, separator
			"foreground": '#ba7330'
		}
	},
	"TNotebook.Tab": {
		"configure": {
			"background": '#db8441',  # tab color when not selected
			"padding": [10, 2],  # [space between text and horizontal tab-button border, space between text and vertical tab_button border]
			"font": "black",
			"highlighthickness": 0
		},
		"map": {
			"background": [("selected", '#f6b05b')],  # Tab color when selected
			"expand": [("selected", [1, 1, 1, 0])]  # text margins
		}
	},
})

s.theme_use('pastel')

# Create Tabs
my_notebook = ttk.Notebook(root,)
my_notebook.pack(pady=0)

# Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

currency_frame.configure(background='#eab676')
conversion_frame.configure(background='#eab676')

# Add our Tabs
my_notebook.add(currency_frame, text="Currencies",)
my_notebook.add(conversion_frame, text="Convert")

# Disable 2nd tab
my_notebook.tab(1, state='disabled')

#######################
# CURRENCY STUFF
#######################

def lock():
	if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
		messagebox.showwarning("WARNING!", "You Didn't Fill Out All The Fields")
	else:
		# Disable entry boxes
		home_entry.config(state="disabled")
		conversion_entry.config(state="disabled")
		rate_entry.config(state="disabled")
		# Enable tab
		my_notebook.tab(1, state='normal')
		# Change Tab Field
		convert_button.config(text=f'Convert From {home_entry.get()}')
def unlock():
	# Enable entry boxes
	home_entry.config(state="normal")
	conversion_entry.config(state="normal")
	rate_entry.config(state="normal")
	# Disable Tab
	my_notebook.tab(1, state='disabled')

home = LabelFrame(currency_frame,)
home.pack(pady=20)
home.configure(background='#eab676', borderwidth=0)

# Home currency label
conversion_label = Label(home, text="Your Home Currency:", font=tkfont.Font(family='Ubuntu', size=14), justify="center", background='#eab676')
conversion_label.pack(pady=10)

# Home currency entry box
home_entry = Entry(home, font=tkfont.Font(family='Ubuntu Condensed', size=24), justify="center",  bg="#f6b05b", selectbackground="#db8441", highlightbackground="#ba7330", highlightcolor="#ba7330", borderwidth=0, highlightthickness=2, disabledbackground= '#ec9552', disabledforeground="#ba7330")
home_entry.pack(pady=10, padx=10)

# Conversion Currency Frame
conversion = LabelFrame(currency_frame,)
conversion.pack(pady=20)
conversion.configure(background='#eab676', borderwidth=0)

# convert to label
conversion_label = Label(conversion, text="Currency To Convert To:", font=tkfont.Font(family='Ubuntu', size=14),  justify="center",background='#eab676')
conversion_label.pack(pady=10)

# Convert To Entry
conversion_entry = Entry(conversion, font=tkfont.Font(family='Ubuntu Condensed', size=24), justify="center",  bg="#f6b05b", selectbackground="#db8441", highlightbackground="#ba7330", highlightcolor="#ba7330", borderwidth=0, highlightthickness=2, disabledbackground= '#ec9552', disabledforeground="#ba7330")
conversion_entry.pack(pady=10, padx=10)

# rate label
rate_label = Label(conversion, text="Current Conversion Rate:", font=tkfont.Font(family='Ubuntu', size=14), justify="center", background='#eab676')
rate_label.pack(pady=10)

# Rate To Entry
rate_entry = Entry(conversion, font=tkfont.Font(family='Ubuntu Condensed', size=24), justify="center", bg="#f6b05b", selectbackground="#db8441", highlightbackground="#ba7330", highlightcolor="#ba7330", borderwidth=0, highlightthickness=2, disabledbackground= '#ec9552', disabledforeground="#ba7330")
rate_entry.pack(pady=10, padx=10)

# Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)
button_frame.configure(background='#eab676')

# Create Buttons
lock_button = Button(button_frame, image=lock_btn, borderwidth=0, background='#eab676', highlightthickness=0, activebackground='#eab676', command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, image=unlock_btn, borderwidth=0, background='#eab676', highlightthickness=0, activebackground='#eab676', command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

#######################
# CONVERSION STUFF
#######################
def convert():
	converted_entry.config(state="normal")

	# Clear Converted Entry Box
	converted_entry.delete(0, END)

	# Conversion Label
	conv_label = str(conversion_entry.get())

	# Convert
	conversion = float(rate_entry.get()) * float(amount_entry.get())

	# Convert to two decimals and Add Commas
	conversion = '{:,.2f}'.format(conversion)


	# Update entry box
	converted_entry.insert(0, f'{conv_label} {conversion}')

	converted_entry.config(state="readonly")

def clear():
	converted_entry.config(state="normal")
	amount_entry.delete(0, END)
	converted_entry.delete(0, END)
	converted_entry.config(state="readonly")

amount = LabelFrame(conversion_frame,)
amount.pack(pady=20)
amount.configure(background='#eab676', borderwidth=0)

amount_label = Label(amount, text="Amount to convert:", font=tkfont.Font(family='Ubuntu', size=14), justify="center", background='#eab676', borderwidth=0)
amount_label.pack(pady=20)

# Entry Box For Amount
amount_entry = Entry(amount, font=tkfont.Font(family='Ubuntu Condensed', size=24), justify="center",  bg="#f6b05b", selectbackground="#db8441", highlightbackground="#ba7330", highlightcolor="#ba7330", borderwidth=0, highlightthickness=2)
amount_entry.pack(pady=10, padx=10)

# Conversion Currency Frame
output = LabelFrame(conversion_frame,)
output.pack(pady=20)
output.configure(background='#eab676', borderwidth=0)

# Convert Button
convert_button = Button(amount, image=conv_btn, borderwidth=0, background='#eab676', highlightthickness=0, activebackground='#eab676', command=convert)
convert_button.pack(pady=20)

# Equals Frame
converted_label = Label(output, text="Converted Amount:", font=tkfont.Font(family='Ubuntu', size=14), justify="center", background='#eab676', borderwidth=0)
converted_label.pack(pady=20)

# Converted entry
converted_entry = Entry(output, font=tkfont.Font(family='Ubuntu Condensed', size=24), justify="center", bg="#f6b05b",  selectbackground="#f6b05b", highlightbackground="#ba7330", readonlybackground="#f6b05b", highlightcolor="#ba7330", borderwidth=0, highlightthickness=2)
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(conversion_frame, image=clear_btn, borderwidth=0, background='#eab676', highlightthickness=0, activebackground='#eab676', command=clear)
clear_button.pack(pady=20)

# Fake Label for spacing
spacer = Label(conversion_frame, text="", width=68, background='#eab676')
spacer.pack()


root.mainloop()
