# IMPORTS
import matplotlib.animation as animation
import tkinter as tk
from pylab import *
from PIL import ImageTk, Image
from ttkthemes import themed_tk as TK
from tkinter import ttk, messagebox
import random


class Initial_input:  # Initial Input class for creating the GUI.

    def __init__(self, master):
        self.master = master
        master.title("Sorting Simulator")
        master.iconbitmap(r'C:\\Users\\rpriy\\Desktop\\SRS\\sort.ico')
        # for positioning of the GUI
        positionRight = int(master.winfo_screenwidth() /
                            2 - master.winfo_reqwidth() / 2)
        positionDown = int(master.winfo_screenheight() /
                           2 - master.winfo_reqheight() / 2)
        master.geometry(f"400x200+{positionRight}+{positionDown}")
        main = ttk.Frame()
        main.pack(side="top", expand=True)

        self.noOfintegers = ""
        self.maxLimit = ""
        self.minLimit = ""
        self.sortmethod = ""

        self.noOFint_label = ttk.Label(main, text="Number of Integers")
        self.noOFint_label.grid(row=0, column=0, pady=2)
        self.noOFint_entry = ttk.Entry(main, width=15)
        self.noOFint_entry.grid(row=0, column=1, padx=5, pady=2)
        self.noOFint_entry.focus()
        self.noOFint_entry.bind('<Return>', self.storing_noofint)
        self.noOFint_button = ttk.Button(
            main, text="Submit", command=self.storing_noofint_submit)
        self.noOFint_button.grid(row=0, column=2, padx=5, pady=2)

        self.minlimit_label = ttk.Label(main, text="Minimum Limit")
        self.minlimit_label.grid(row=1, column=0, pady=2)
        self.minlimit_entry = ttk.Entry(main, width=15)
        self.minlimit_entry.grid(row=1, column=1, padx=5, pady=2)
        self.minlimit_entry.focus()
        self.minlimit_entry.bind('<Return>', self.storing_minint)
        self.minlimit_button = ttk.Button(
            main, text="Submit", command=self.storing_minint_submit)
        self.minlimit_button.grid(row=1, column=2, padx=5, pady=2)

        self.maxlimit_label = ttk.Label(main, text="Maximum Limit")
        self.maxlimit_label.grid(row=2, column=0, pady=2)
        self.maxlimit_entry = ttk.Entry(main, width=15)
        self.maxlimit_entry.grid(row=2, column=1, padx=5, pady=2)
        self.maxlimit_entry.focus()
        self.maxlimit_entry.bind('<Return>', self.storing_maxint)
        self.maxlimit_button = ttk.Button(
            main, text="Submit", command=self.storing_maxint_submit)
        self.maxlimit_button.grid(row=2, column=2, padx=5, pady=2)

        self.sortingmethod_label = ttk.Label(
            main, text="Choose sorting method: ")
        self.sortingmethod_label.grid(row=3, column=0, pady=2)
        self.sortingmethod_dropdown = ttk.Combobox(main, values=["Insertion Sort", "Bubble Sort",
                                                                 "Quick Sort", "Merge Sort",
                                                                 "Selection Sort"], state="readonly")
        self.sortingmethod_dropdown.grid(row=3, column=1, padx=5, pady=2)
        self.sortingmethod_dropdown.current(0)
        self.visualize_button = ttk.Button(
            main, text="VISUALIZE!", command=self.storing_method)
        self.visualize_button.grid(row=4, column=1, padx=3, pady=10)

    def storing_noofint(self, event):
        self.noOfintegers = self.noOFint_entry.get()
        if self.noOfintegers == '':
            messagebox.showerror(
                "Error", "Number of integers cannot be empty. \nTry Again!")
        elif int(self.noOfintegers) <= 0:
            messagebox.showerror(
                "Error", "Number of integers cannot be a negative number. \nTry Again!")
        else:
            pass

    def storing_noofint_submit(self):
        self.noOfintegers = self.noOFint_entry.get()
        if self.noOfintegers == '':
            messagebox.showerror(
                "Error", "Number of integers cannot be empty. \nTry Again!")
        elif int(self.noOfintegers) <= 0:
            messagebox.showerror(
                "Error", "Number of integers cannot be a negative number. \nTry Again!")
        else:
            pass

    def storing_maxint(self, event):
        self.maxLimit = self.maxlimit_entry.get()
        if self.noOfintegers == '':
            messagebox.showerror(
                "Error", "Number of integers cannot be empty. \nTry Again!")
        elif self.minLimit == '':
            messagebox.showerror(
                "Error", "Minimum Limit cannot be empty. \nTry Again!")
        elif self.maxLimit == '':
            messagebox.showerror(
                "Error", "Maximum Limit cannot be empty. \nTry Again!")
        elif int(self.maxLimit) <= int(self.minLimit):
            messagebox.showerror(
                "Error", "Maximum Limit should be greater than Minimum Limit. \nTry Again!")
        elif int(self.maxLimit) - int(self.minLimit) < int(self.noOfintegers):
            messagebox.showerror("Error",
                                 "Difference between Max and Min Limits should be greater or equal than the range of integers. \nTry Again!")
        else:
            pass

    def storing_maxint_submit(self):
        self.maxLimit = self.maxlimit_entry.get()
        if self.noOfintegers == '':
            messagebox.showerror(
                "Error", "Number of integers cannot be empty. \nTry Again!")
        elif self.minLimit == '':
            messagebox.showerror(
                "Error", "Minimum Limit cannot be empty. \nTry Again!")
        elif self.maxLimit == '':
            messagebox.showerror(
                "Error", "Maximum Limit cannot be empty. \nTry Again!")
        elif int(self.maxLimit) <= int(self.minLimit):
            messagebox.showerror(
                "Error", "Maximum Limit should be greater than Minimum Limit. \nTry Again!")
        elif int(self.maxLimit) - int(self.minLimit) < int(self.noOfintegers):
            messagebox.showerror("Error",
                                 "Difference between Max and Min Limits should be greater or equal than the range of integers. \nTry Again!")
        else:
            pass

    def storing_minint(self, event):
        self.minLimit = self.minlimit_entry.get()
        if self.noOfintegers == '':
            messagebox.showerror(
                "Error", "Number of integers cannot be empty. \nTry Again!")
        elif int(self.noOfintegers) < 0:
            messagebox.showerror(
                "Error", "Number of integers cannot be a negative number. \nTry Again!")
        elif int(self.minLimit) < 0:
            messagebox.showerror(
                "Error", "Minimum limit cannot be a negative number. \nTry Again!")
        else:
            pass

    def storing_minint_submit(self):
        self.minLimit = self.minlimit_entry.get()
        if self.noOfintegers == '':
            messagebox.showerror(
                "Error", "Number of integers cannot be empty. \nTry Again!")
        elif int(self.noOfintegers) < 0:
            messagebox.showerror(
                "Error", "Number of integers cannot be a negative number. \nTry Again!")
        elif int(self.minLimit) < 0:
            messagebox.showerror(
                "Error", "Minimum limit cannot be a negative number. \nTry Again!")
        else:
            pass

    def storing_method(self):
        count = 0
        self.sortmethod = self.sortingmethod_dropdown.get()
        if self.noOfintegers == '':
            messagebox.showerror(
                "Error", "Number of integers cannot be empty. \nTry Again!")
            count += 1
        if self.minLimit == '':
            messagebox.showerror(
                "Error", "Minimum Limit cannot be empty. \nTry Again!")
            count += 1
        if self.maxLimit == '':
            messagebox.showerror(
                "Error", "Maximum Limit cannot be empty. \nTry Again!")
            count += 1
        if count == 0:
            new_class = Algo_select()

    def return_noOfintegers(self):
        return int(self.noOfintegers)

    def return_minLimit(self):
        return int(self.minLimit)

    def return_maxLimit(self):
        return int(self.maxLimit)

    def return_sortMethod(self):
        return self.sortmethod


class Algo_select(Initial_input):

    def __init__(self):
        self.no_of_int = Initial.return_noOfintegers()
        self.max_limit = Initial.return_maxLimit()
        self.min_limit = Initial.return_minLimit()
        self.sort_method = Initial.return_sortMethod()
        self.newClass()

    def newClass(self):
        self.list = self.create_list()
        vis = Vis_algo(self.list, self.no_of_int,
                       self.sort_method, self.max_limit, self.min_limit)

    def create_list(self):
        # Build and randomly shuffle list of integers.
        self.rand_list = [random.randrange(self.min_limit, self.max_limit)
                          for x in range(self.no_of_int)]
        return self.rand_list


class Vis_algo():

    def __init__(self, l, n, m, maxL, minL):
        self.random_list = l
        self.numOf_int = n
        self.sort_Method = m
        self.max_Limit = maxL
        self.min_Limit = minL
        self.visualize_fun(self.random_list, self.numOf_int, self.sort_Method)

    def swap(self, A, i, j):
        """Helper function to swap elements i and j of list A."""

        if i != j:
            A[i], A[j] = A[j], A[i]

    def bubblesort(self, A):
        """In-place bubble sort."""

        if len(A) == 1:
            return

        swapped = True
        for i in range(len(A) - 1):
            if not swapped:
                break
            swapped = False
            for j in range(len(A) - 1 - i):
                if A[j] > A[j + 1]:
                    self.swap(A, j, j + 1)
                    swapped = True
                yield A

    def insertionsort(self, A):
        """In-place insertion sort."""

        for i in range(1, len(A)):
            j = i
            while j > 0 and A[j] < A[j - 1]:
                self.swap(A, j, j - 1)
                j -= 1
                yield A

    def mergesort(self, A, start, end):
        """Merge sort."""

        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from self.mergesort(A, start, mid)
        yield from self.mergesort(A, mid + 1, end)
        yield from self.merge(A, start, mid, end)
        yield A

    def merge(self, A, start, mid, end):
        """Helper function for merge sort."""

        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if A[leftIdx] < A[rightIdx]:
                merged.append(A[leftIdx])
                leftIdx += 1
            else:
                merged.append(A[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(A[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(A[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            A[start + i] = sorted_val
            yield A

    def quicksort(self, A, start, end):
        """In-place quicksort."""

        if start >= end:
            return

        pivot = A[end]
        pivotIdx = start

        for i in range(start, end):
            if A[i] < pivot:
                self.swap(A, i, pivotIdx)
                pivotIdx += 1
            yield A
        self.swap(A, end, pivotIdx)
        yield A

        yield from self.quicksort(A, start, pivotIdx - 1)
        yield from self.quicksort(A, pivotIdx + 1, end)

    def selectionsort(self, A):
        """In-place selection sort."""
        if len(A) == 1:
            return

        for i in range(len(A)):
            # Find minimum unsorted value.
            minVal = A[i]
            minIdx = i
            for j in range(i + 1, len(A)):
                if A[j] < minVal:
                    minVal = A[j]
                    minIdx = j
            self.swap(A, i, minIdx)
            yield A

    def createNewWindow(self, st):
        """Function to create new window for displaying additional information"""
        plt.close('all')
        newWindow = tk.Toplevel(root)
        newWindow.title(f"{st} Sort")
        # To position this new window
        positionR = int(newWindow.winfo_screenwidth() /
                        2 - newWindow.winfo_reqwidth() / 2)
        positionD = int(newWindow.winfo_screenheight() /
                        2 - newWindow.winfo_reqheight() / 2)
        if st == "Bubble":
            newWindow.geometry(f"700x512+{positionR + 100}+{positionD - 200}")
            load = Image.open(
                "C:\\Users\\rpriy\\Desktop\\SRS\\bubble-sort.jpg")
        elif st == "Insertion":
            newWindow.geometry(f"694x501+{positionR + 100}+{positionD - 190}")
            load = Image.open(
                "C:\\Users\\rpriy\\Desktop\\SRS\\insertion-sort.jpg")
        elif st == "Merge":
            newWindow.geometry(f"800x589+{positionR + 20}+100")
            load = Image.open("C:\\Users\\rpriy\\Desktop\\SRS\\merge-sort.jpg")
        elif st == "Quick":
            newWindow.geometry(f"700x571+{positionR + 100}+{positionD - 230}")
            load = Image.open("C:\\Users\\rpriy\\Desktop\\SRS\\quick-sort.jpg")
        else:
            newWindow.geometry(f"797x683+{positionR + 20}+50")
            load = Image.open(
                "C:\\Users\\rpriy\\Desktop\\SRS\\selection-sort.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(newWindow, image=render)
        img.image = render
        img.place(x=0, y=0)

    def visualize_fun(self, l, n, method):
        """Function which visualizes the algorithm"""
        graph = ""
        # Selecting the correct option to get the appropriate generator function
        if method == "Bubble Sort":
            title = "Bubble sort"
            graph = "bs"
            self.createNewWindow("Bubble")
            gen_func = self.bubblesort(l)
        elif method == "Insertion Sort":
            title = "Insertion sort"
            graph = "is"
            self.createNewWindow("Insertion")
            gen_func = self.insertionsort(l)
        elif method == "Merge Sort":
            title = "Merge sort"
            graph = "ms"
            self.createNewWindow("Merge")
            gen_func = self.mergesort(l, 0, n - 1)
        elif method == "Quick Sort":
            title = "Quick sort"
            graph = "qs"
            self.createNewWindow("Quick")
            gen_func = self.quicksort(l, 0, n - 1)
        else:
            title = "Selection sort"
            graph = "ss"
            self.createNewWindow("Selection")
            gen_func = self.selectionsort(l)

        # Initialize figure and axis.
        fig, ax = plt.subplots()

        ax.set_title(title)

        # Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
        # list of rectangles (with each bar in the bar plot corresponding
        # to one rectangle), which is stored in bar_rects.
        bar_rects = ax.bar(range(len(l)), l, align="edge")

        # Set axis limits. Set y axis upper limit high enough that the tops of
        # the bars won't overlap with the text label.
        ax.set_xlim(0, n)
        ax.set_ylim(0, (1.05 * self.max_Limit))

        iteration = [0]

        # update figure function for matplotlib animation 
        def update_fig(a, rects, iteration):
            for rect, val in zip(rects, a):
                rect.set_height(val)
                y_pos = np.arange(len(a))
                plt.xticks(y_pos, a, ha='left', size="small")

        anim = animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(
                                           bar_rects, iteration), frames=gen_func, interval=200,
                                       repeat=False)

        # This is done to position the graph
        thismanager = plt.get_current_fig_manager()

        if graph == "bs":
            thismanager.window.wm_geometry("+126+130")
        elif graph == "is":
            thismanager.window.wm_geometry("+126+130")
        elif graph == "ms":
            thismanager.window.wm_geometry("+46+130")
        elif graph == "qs":
            thismanager.window.wm_geometry("+126+130")
        else:
            thismanager.window.wm_geometry("+46+130")

        plt.show()


root = TK.ThemedTk()
root.get_themes()
root.set_theme("plastik")
Initial = Initial_input(root)
root.mainloop()
