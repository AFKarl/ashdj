from cgitb import text
import tkinter as tk
from tkinter.font import BOLD
from turtle import back

class stopwatch(tk.Frame):

    def __init__(self,window=None):
        super().__init__(window)
        self.window = window
        self.new_time = ""
        self.running = False
        self.total_minutes = 0
        self.total_seconds = 0
        self.total_miliseconds = 0
        self.pack
        self.laps = 0
        self.features()
