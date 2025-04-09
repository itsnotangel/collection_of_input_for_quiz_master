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
            choice_frame = tk.Frame(root)
            choice_frame.pack(fill=tk.X, padx=20, pady=5)

            choice_label = tk.Label(choice_frame, text=f"{self.choice_labels[i]}:", anchor="w")
            choice_label.pack(side=tk.LEFT, padx=5)

            # Adding an entry box for each choice (A, B, C, D)
            entry = tk.Entry(choice_frame)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.choice_entries.append(entry)

        # Creating a save button to save the user's inputted question, answer, and choices
        self.save_button = tk.Button(root, text="Save", width=15, command=self.save_all_inputs)
        self.save_button.pack(side=tk.LEFT, padx=(0,10))

        # Creating an exit button to close the application (The Quizzler Maker)
        self.exit_button = tk.Button(root, text="Exit", width=15, command=self.exit_program)
        self.exit_button.pack(side=tk.RIGHT, padx=(10,0))

        # Create a storage for questions, answer, and choices from the user
        self.question_answer_choices = []
    
    def save_all_inputs(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        choices = [entry.get() for entry in self.choice_entries]

        # Validation of inputs
        if not question:
            messagebox.showerror("ERROR!", "Question block cannot be empty.")

        elif not answer:
            messagebox.showerror("ERROR!", "Answer block cannot be empty.")

        if "" in choices:
            messagebox.showerror("ERROR!", "All choices must be filled.")

        question_answer_choices_data = {
            "question": question,
            "answer": answer,
            "choices": choices
        }

        self.question_answer_choices.append(question_answer_choices_data)
        
    # Exiting the program method
    def exit_program(self):
        self.root.destroy()
        
# Initializes the main Tkinter window and runs the event loop to start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = TheQuizzler(root)
    root.mainloop()