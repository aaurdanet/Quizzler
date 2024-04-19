Quizzler

This is a simple quiz application called Quizzler. It fetches questions from the Open Trivia Database API and allows users to answer them as True or False. Below are the instructions to run the application:
Requirements

Python 3.x
tkinter library (usually comes pre-installed with Python)

How to Run

Make sure you have Python installed on your system.
Download the necessary files: quiz_brain.py, question_model.py, ui.py, and data.py.
Ensure that you have an images folder containing true.png and false.png images for the True and False buttons respectively.
Run the following command in your terminal or command prompt to execute the program:

python main.py

Functionality

The application will start by fetching 10 True/False questions from the Open Trivia Database API.
Each question will be displayed with options to answer True or False.
After answering, the application will provide immediate feedback by changing the background color of the canvas.
Once all questions are answered, the application will display the final score.

Files

quiz_brain.py: Contains the QuizBrain class responsible for managing the quiz logic.
question_model.py: Defines the Question class representing a single question.
ui.py: Implements the QuizInterface class for the graphical user interface using tkinter.
main.py: Acts as the entry point for the application.
data.py: Fetches question data from the Open Trivia Database API.

Acknowledgments

The application utilizes the Open Trivia Database API for fetching quiz questions.
