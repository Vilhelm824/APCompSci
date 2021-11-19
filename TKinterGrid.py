#! /usr/bin/python3
import tkinter as tk

groot = tk.Tk()

blue_frame = tk.Frame(groot, bg="blue", height=100, width=125).grid(row=0, column=0)
red_frame = tk.Frame(groot, bg="red", height=100, width=125).grid(row=1, column=0)
green_frame = tk.Frame(groot, bg="green", height=100, width=75).grid(row=0, column=1)
yellow_frame = tk.Frame(groot, bg="yellow", height=100, width=75).grid(row=1, column=1)

groot.mainloop()
