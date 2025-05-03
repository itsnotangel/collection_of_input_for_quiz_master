# Imported tkinder for GUI components
import tkinter as tk

# Imported messagebox for pop-up messages
from tkinter import messagebox

# The Quizzler class definition, which sets up the main app window and specific dimension
class TheQuizzler:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")

        # Adding the main title 
        main_title_label = tk.Label(text="THE QUIZZLER", font=("Arial", 30, "bold"), fg="darkred")
        main_title_label.pack(fill=tk.X, pady=(10, 0))

        # Adding the subtitle
        sub_title_label = tk.Label(text="THE ULTIMATE QUIZ EDITION", font=("Arial", 20, "bold"), fg="darkred")
        sub_title_label.pack(fill=tk.X, pady=(0, 10))

# Initializes the main Tkinter window and runs the event loop to start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = TheQuizzler(root)
    root.mainloop()