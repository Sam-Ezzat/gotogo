from tkinter import Tk, Canvas, Button, Label, StringVar, Frame
import random
import time
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort

class SortingApp:
    def __init__(self, master):
        self.master = master
        master.title("Sorting Algorithms Visualization")

        self.canvas = Canvas(master, width=600, height=400)
        self.canvas.pack()

        self.sorting_label = Label(master, text="Select a sorting algorithm:")
        self.sorting_label.pack()

        self.algorithm_var = StringVar(value="Quick Sort")
        self.algorithm_menu = Button(master, textvariable=self.algorithm_var, command=self.select_algorithm)
        self.algorithm_menu.pack()

        self.start_button = Button(master, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack()

        self.numbers = [random.randint(1, 100) for _ in range(50)]
        self.draw_numbers()

    def select_algorithm(self):
        algorithms = ["Quick Sort", "Merge Sort", "Bubble Sort", "Insertion Sort"]
        current_index = algorithms.index(self.algorithm_var.get())
        next_index = (current_index + 1) % len(algorithms)
        self.algorithm_var.set(algorithms[next_index])

    def draw_numbers(self):
        self.canvas.delete("all")
        bar_width = 10
        for i, number in enumerate(self.numbers):
            self.canvas.create_rectangle(i * bar_width, 400 - number * 4, (i + 1) * bar_width, 400, fill="blue")

    def start_sorting(self):
        algorithm = self.algorithm_var.get()
        if algorithm == "Quick Sort":
            self.numbers = quick_sort(self.numbers)
        elif algorithm == "Merge Sort":
            self.numbers = merge_sort(self.numbers)
        elif algorithm == "Bubble Sort":
            self.numbers = bubble_sort(self.numbers)
        elif algorithm == "Insertion Sort":
            self.numbers = insertion_sort(self.numbers)

        self.draw_numbers()

if __name__ == "__main__":
    root = Tk()
    app = SortingApp(root)
    root.mainloop()