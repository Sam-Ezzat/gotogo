def main():
    import tkinter as tk
    from tkinter import messagebox
    from algorithms.quick_sort import quick_sort
    from algorithms.merge_sort import merge_sort
    from algorithms.bubble_sort import bubble_sort
    from algorithms.insertion_sort import insertion_sort
    import random

    def sort_and_display(algorithm):
        numbers = [random.randint(0, 100) for _ in range(10)]
        if algorithm == "Quick Sort":
            sorted_numbers = quick_sort(numbers)
        elif algorithm == "Merge Sort":
            sorted_numbers = merge_sort(numbers)
        elif algorithm == "Bubble Sort":
            sorted_numbers = bubble_sort(numbers)
        elif algorithm == "Insertion Sort":
            sorted_numbers = insertion_sort(numbers)
        
        messagebox.showinfo("Sorted Numbers", f"Unsorted: {numbers}\nSorted: {sorted_numbers}")

    root = tk.Tk()
    root.title("Sorting Algorithms Visualization")

    tk.Label(root, text="Choose a sorting algorithm:").pack()

    algorithms = ["Quick Sort", "Merge Sort", "Bubble Sort", "Insertion Sort"]
    for algo in algorithms:
        button = tk.Button(root, text=algo, command=lambda a=algo: sort_and_display(a))
        button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()