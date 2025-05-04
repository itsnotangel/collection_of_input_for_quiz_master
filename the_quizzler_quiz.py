# Imported tkinder for GUI components
import tkinter as tk

# Imported messagebox for pop-up messages
from tkinter import messagebox

# The Quizzler class definition, which sets up the main app window and specific dimension
class TheQuizzler:
    def __init__(self, root):
        self.root = root
        self.root.title("The Quizzler - The Ultimate Quiz Edition")
        self.root.geometry("600x600")

        # Initializing variables needed
        self.questions = []
        self.current_question = None
        self.current_question_index = 0
        self.score = 0
        self.total_questions = 0

        # Creating the main frame 
        main_frame = tk.Frame(root, bd=5, relief="groove", padx=20, pady="20")
        main_frame.pack(fill="both", padx=20, pady=20)

        # Adding the main title 
        main_title_label = tk.Label(main_frame, text="THE QUIZZLER", font=("Arial", 30, "bold"), fg="darkred")
        main_title_label.pack(fill=tk.X, pady=(10, 0))

        # Adding the subtitle
        sub_title_label = tk.Label(main_frame, text="THE ULTIMATE QUIZ EDITION", font=("Arial", 20, "bold"), fg="darkred")
        sub_title_label.pack(fill=tk.X, pady=(0, 10))

        # Creating a frame for the question
        self.question_frame = tk.Frame(main_frame)
        self.question_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 12), wraplength=500, justify="left")
        self.question_label.pack(fill=tk.X, pady=10)

        # Creating a score display
        self.score_label = tk.Label(main_frame, text="Score: 0/0", font=("Arial", 12, "bold"), fg="darkred")
        self.score_label.pack(fill=tk.X, pady=(0, 10))

        # Instruction label to guide user how to use the application
        instruction_label = tk.Label(main_frame, text="Instruction: Select the correct answer from the four choices.", font=("Arial", 10), fg="grey")
        instruction_label.pack(fill=tk.X, pady=(0, 5))

        # Creating a frame for each of the choices
        self.choices_frame = tk.Frame(main_frame)
        self.choices_frame.pack(fill=tk.X, padx=20, pady=10)

        # Adding a label for each choice (From A to D)
        self.choice_buttons = []
        self.choice_labels = ["A", "B", "C", "D"]
        
        for i in range(4):
            choice_frame = tk.Frame(self.choices_frame)
            choice_frame.pack(fill=tk.X, pady=5)

            button = tk.Button(
                choice_frame,
                text=f"{self.choice_labels[i]}. ",
                font=("Arial", 10, "bold"),
                anchor="w",
                width=30,
                fg="darkred",
            )
            button.pack(fill=tk.X)

        # Creating a "Next Question" button to move on to the next question
        self.next_question_button = tk.Button(
            main_frame,
            text="NEXT QUESTION",
            font =("Arial", 10, "bold"),
            fg="darkred",
            width=15,
        )
        self.next_question_button.pack(pady=(10,0))

        # Creating exit button to close the application
        self.exit_button = tk.Button(
            main_frame,
            text="EXIT",
            font=("Arial", 10, "bold"),
            fg="darkred",
            width=15,
            command=self.root.destroy
        )
        self.exit_button.pack(pady=(10, 0))

    # Created a function that reads questions from a text file and adds those to the Quizzler
    def load_questions(self):
        try:
            # Opening and reading the quiz data file
            with open("data_for_the_quizzler.txt", "r") as file:
                content = file.read()
                
            sections = content.split("-" * 30)
            
            for section in sections:
                if not section.strip():
                    continue
                    
                lines = section.strip().split("\n")
                if len(lines) < 7:  
                    continue
                    
                # Getting the question text from line 1
                question_text = lines[0].replace("Question", "", 1).split(":", 1)[1].strip()
                
                # Getting the correct answer from line 2
                answer = lines[1].split(":", 1)[1].strip()
                
                # Getting choices from lines 4 to 7
                choices = []
                for i in range(3, 7):  
                    if i < len(lines):
                        choice = lines[i].split(":", 1)[1].strip()
                        choices.append(choice)
                
                # Adding to questions list
                if question_text and answer and len(choices) == 4:
                    self.questions.append({
                        "question": question_text,
                        "answer": answer,
                        "choices": choices
                    })

            # Updating the total question count
            self.total_questions = len(self.questions)
        
        # Showing popup message if the file is missing
        except FileNotFoundError:
            messagebox.showerror("ERROR!", "Quiz data file not found.")

# Initializes the main Tkinter window and runs the event loop to start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = TheQuizzler(root)
    root.mainloop()