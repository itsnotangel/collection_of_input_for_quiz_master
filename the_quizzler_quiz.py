# Import tkinter for GUI components
import tkinter as tk

# Import messagebox for pop-up messages
from tkinter import messagebox

# Import random for randomizing question selection
import random

# The main application class for the quiz
class TheQuizzlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Quizzler - The Ultimate Quiz Edition")
        self.root.geometry("600x530")

        # Initialize variables needed
        self.quiz_questions = []
        self.current_question = None
        self.current_question_index = 0
        self.score_count = 0
        self.total_questions = 0

        # Create the main frame 
        main_frame = tk.Frame(root, bd=5, relief="groove", padx=20, pady=20)
        main_frame.pack(fill="both", padx=20, pady=20)

        # Create the main title 
        main_title_label = tk.Label(main_frame, text="THE QUIZZLER", font=("Arial", 30, "bold"), fg="darkred")
        main_title_label.pack(fill=tk.X, pady=(10, 0))

        # Create the subtitle
        sub_title_label = tk.Label(main_frame, text="THE ULTIMATE QUIZ EDITION", font=("Arial", 20, "bold"), fg="darkred")
        sub_title_label.pack(fill=tk.X, pady=(0, 10))

        # Create a frame for the question
        self.question_frame = tk.Frame(main_frame)
        self.question_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 12), wraplength=500, justify="left")
        self.question_label.pack(fill=tk.X, pady=10)

        # Question label to display the current question
        self.score_label = tk.Label(main_frame, text="Score: 0/0", font=("Arial", 12, "bold"), fg="darkred")
        self.score_label.pack(fill=tk.X, pady=(0, 10))

        # Instruction label to guide user how to use the application
        instruction_label = tk.Label(main_frame, text="Instruction: Select the correct answer from the four choices.", font=("Arial", 10), fg="grey")
        instruction_label.pack(fill=tk.X, pady=(0, 5))

        # Create a frame for each of the choices
        self.choices_frame = tk.Frame(main_frame)
        self.choices_frame.pack(fill=tk.X, padx=20, pady=10)

        # Add a label for each choice (From A to D)
        self.choice_buttons = []
        self.choice_labels = ["A", "B", "C", "D"]
        
        for i in range(4):
            choice_frame = tk.Frame(self.choices_frame)
            choice_frame.pack(fill=tk.X, pady=5)

            button = tk.Button(
                choice_frame,
                text=f"{self.choice_labels[i]}.",
                font=("Arial", 10, "bold"),
                anchor="w",
                width=30,
                fg="darkred",
                command=lambda idx=i: self.check_answer(self.choice_labels[idx])
            )
            button.pack(fill=tk.X)
            self.choice_buttons.append(button)

        # Creating a "Next Question" button to move on to the next question
        self.next_question_button = tk.Button(
            main_frame,
            text="NEXT QUESTION",
            font=("Arial", 10, "bold"),
            fg="black",
            width=15,
            command=self.next_question
        )
        self.next_question_button.pack(side=tk.LEFT, padx=20, pady=(10, 0))

        # Create an exit button to close the application
        self.exit_button = tk.Button(
            main_frame,
            text="EXIT QUIZ",
            font=("Arial", 10, "bold"),
            fg="black",
            width=15,
            command=self.root.destroy
        )
        self.exit_button.pack(side=tk.RIGHT, padx=20, pady=(10, 0))

        # Create a function to load questions from a text file
        self.load_questions()

        # Start the quiz if there are questions available
        if self.quiz_questions:
            self.next_question()
        else:
            messagebox.showerror("ERROR!", "There are no questions found. Make sure that you created questions.")
            root.destroy()

    # Create a function that reads questions from a text file and adds those to the Quizzler
    def load_questions(self):
        try:
            # Open and read the quiz data file
            with open("data_for_the_quizzler.txt", "r") as file:
                content = file.read()
                
            sections = content.split("-" * 30)
            
            for section in sections:
                if not section.strip():
                    continue
                    
                lines = section.strip().split("\n")
                if len(lines) < 7:  
                    continue
                    
                # Get the question text from line 1
                question_text = lines[0].replace("Question", "", 1).split(":", 1)[1].strip()
                
                # Get the correct answer from line 2
                answer = lines[1].split(":", 1)[1].strip()
                
                # Get choices from lines 4 to 7
                choices = []
                for i in range(3, 7):  
                    if i < len(lines):
                        choice = lines[i].split(":", 1)[1].strip()
                        choices.append(choice)
                
                # Add to questions list
                if question_text and answer and len(choices) == 4:
                    self.quiz_questions.append({
                        "question": question_text,
                        "answer": answer,
                        "choices": choices
                    })

            # Update the total question count
            self.total_questions = len(self.quiz_questions)
        
        # Show popup message if the file is missing
        except FileNotFoundError:
            messagebox.showerror("ERROR!", "Quiz data file not found.")
            
    def next_question(self):
        # Enable all choice buttons
        for button in self.choice_buttons:
            button.config(state=tk.NORMAL)
        
        # Select a random question if there are any left
        if self.quiz_questions:
            self.current_question_index = random.randint(0, len(self.quiz_questions) - 1)
            self.current_question = self.quiz_questions.pop(self.current_question_index)
            
            # Display the question
            self.question_label.config(text=self.current_question["question"])
            
            # Update choice buttons with the choices
            for i in range(4):
                self.choice_buttons[i].config(text=f"{self.choice_labels[i]}. {self.current_question['choices'][i]}")
            
            # Update score display
            self.score_label.config(text=f"Score: {self.score_count}/{self.total_questions - len(self.quiz_questions)}")
        else:
            # If no more questions, show final score
            self.question_label.config(text=f"Quiz completed! Final score: {self.score_count}/{self.total_questions}")
            for button in self.choice_buttons:
                button.config(state=tk.DISABLED)
            self.next_question_button.config(state=tk.DISABLED)

    # Function to check the user's selected answer
    def check_answer(self, selected_answer):
        if self.current_question:
            correct_answer = self.current_question["answer"].upper()

            if selected_answer == correct_answer:
                self.score_count += 1
                messagebox.showinfo("CORRECT!", "You selected the correct answer!")
            else:
                messagebox.showerror("INCORRECT!", f"The correct answer to that is {correct_answer}.")
            
            # Disabling all choice buttons after an answer is selected
            for button in self.choice_buttons:
                button.config(state=tk.DISABLED)

            # Updating the score display
            self.score_label.config(text=f"Score: {self.score_count}/{self.total_questions - len(self.quiz_questions)}")

# Initializes the main Tkinter window and runs the event loop to start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = TheQuizzlerApp(root)
    root.mainloop()