import tkinter as tk
import matplotlib
matplotlib.use('Agg')


window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
