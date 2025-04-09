# Imported the libraries
import tkinter as tk
from tkinter import messagebox

# The Quizzler class definition, which sets up the main app window and specific dimension
class TheQuizzler:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")

        # Adding the main title of the window
        main_title_label = tk.Label(root, text="WELCOME TO THE QUIZZLER", font=("Arial", 18))
        main_title_label.pack(fill=tk.X, pady=(10, 0))

        # Adding the question box for user to input their questions
        tk.Label(text="Question:", anchor="w").pack(fill=tk.X, padx=20, pady=(10, 0))
        self.question_entry = tk.Entry(root)
        self.question_entry.pack(fill=tk.X, padx=18)

        # Adding the answer box for user to input the correct answer
        tk.Label(text="Correct Answer:", anchor="w").pack(fill=tk.X, padx=20, pady=(10, 0))
        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(fill=tk.X, padx=18)

        # Getting the window size and printing it to the console (Only for checking the size)
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        print(f"Window Size: {window_width}x{window_height}")

        # Adding a "Choices" label text 
        tk.Label(text="Choices:", anchor="w").pack(fill=tk.X, padx=20, pady=(10, 0))

        # Creating a list of entries storing the choices inputted by the user
        self.choice_entries = []

        # Assigning labels for each choice entry (A - D)
        self.choice_labels = ['A', 'B', 'C', 'D']

        # Looping over the choices to assign a labels for each one
        for i in range(4):
            choice_label = tk.Label(text=f"{self.choice_labels[i]}:", anchor="w")
            choice_label.pack(side=tk.LEFT, padx=5)
            
# Initializes the main Tkinter window and runs the event loop to start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = TheQuizzler(root)
    root.mainloop()