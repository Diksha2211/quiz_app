import tkinter as tk
from tkinter import messagebox
import random

# Define the quiz questions, options, and correct answers
questions = [
    "Which river is known as the 'Ganga of the South'?",
    "What is the capital of India?",
    "Which festival is also known as the 'Festival of Lights'?",
    "Who was the first Prime Minister of India?",
    "Which famous monument is located in Agra, India?",
    "Which Indian state is known as the 'Land of Five Rivers'?",
    "What is the national animal of India?",
    "Which Indian cricketer is also known as 'Captain Cool'?",
    "What is the currency of India?",
    "Who wrote the Indian national anthem 'Jana Gana Mana'?",
]

options = [
    ["Godavari", "Krishna", "Yamuna", "Kaveri"],
    ["Mumbai", "Kolkata", "New Delhi", "Chennai"],
    ["Holi", "Dussehra", "Diwali", "Eid"],
    ["Jawaharlal Nehru", "Indira Gandhi", "Mahatma Gandhi", "Rajendra Prasad"],
    ["Taj Mahal", "Qutub Minar", "Red Fort", "Hawa Mahal"],
    ["Rajasthan", "Kerala", "Punjab", "Tamil Nadu"],
    ["Bengal Tiger", "Lion", "Elephant", "Peacock"],
    ["Virat Kohli", "Rahul Dravid", "Sachin Tendulkar", "Mahendra Singh Dhoni"],
    ["Indian Rupee", "Dollar", "Euro", "Yen"],
    ["Rabindranath Tagore", "Bankim Chandra Chattopadhyay", "Sarojini Naidu", "Subramania Bharati"],
]

correct_answers = [
    "Godavari",
    "New Delhi",
    "Diwali",
    "Jawaharlal Nehru",
    "Taj Mahal",
    "Punjab",
    "Bengal Tiger",
    "Mahendra Singh Dhoni",
    "Indian Rupee",
    "Rabindranath Tagore",
]

# Shuffle the questions and answers
quiz_data = list(zip(questions, options, correct_answers))
random.shuffle(quiz_data)

# Create the main application window
root = tk.Tk()
root.title("Indian Quiz")

# Create variables to track question index and score
current_question = 0
score = 0

def check_answer():
    global score, current_question

    selected_answer = answer_var.get()

    if selected_answer == quiz_data[current_question][2]:
        score += 1

    current_question += 1

    if current_question < len(quiz_data):
        show_question()
    else:
        show_result()

def show_question():
    question_label["text"] = quiz_data[current_question][0]

    for i, option in enumerate(quiz_data[current_question][1]):
        option_buttons[i]["text"] = option

def show_result():
    messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(quiz_data)}")
    root.destroy()

# Create the question label
question_label = tk.Label(root, text="", font=("Helvetica", 16))
question_label.pack(pady=20)

# Create option buttons
option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=("Helvetica", 12), command=check_answer)
    button.pack(pady=5)
    option_buttons.append(button)

# Create the answer variable
answer_var = tk.StringVar()
answer_var.set("")

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

show_question()

# Start the main event loop
root.mainloop()

