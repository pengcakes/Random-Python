"""
.
"""
import time




import tkinter as tk
import matplotlib
matplotlib.use('Agg')


window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()



if __name__ == "__main__":
    # need to specify location outside script runtime
    flies_caught = []

    fly_count = 0

    start = time.time()

    days_since_last_seen = 0
    days_since_last_caught = 0

    while(days_since_last_seen < 10 and days_since_last_caught < 6):


        # an interactive gui at all times to input a sighting or a catch


    end = time.time()
    print(end - start)
