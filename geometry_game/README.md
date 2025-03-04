Geometry Game

🚧 Work in Progress 🚧

This project is a Python application that allows users to interact with geometric concepts by providing a coordinate representing a Point and guessing a rectangle's area. The program then draws a rectangle on a canvas using a set of random points, calculates the actual area, and verifies if the user’s provided Point falls within the rectangle.

📌 Overview

This Python-based game utilizes the turtle module for graphical representation and allows users to:

Input a coordinate (X, Y) to check if it falls inside a randomly generated rectangle.

Guess the rectangle’s area.

Visually display the rectangle and point using turtle graphics.

Get feedback on whether the guessed Point is inside the rectangle and how close the area guess is.

⚙️ Features

Randomly generates a rectangle using two random points.

Allows users to input a Point and a guessed area.

Validates if the Point is inside the rectangle.

Displays the rectangle and the user’s Point on a turtle canvas.

Provides feedback on area accuracy and Point validation.

🚀 Installation & Setup

Prerequisites

Make sure you have the following installed:

Python 3.x

Install Dependencies

No additional dependencies are required beyond Python’s standard library.

Run the Application

Clone the repository or download the files.

Open a terminal and navigate to the project folder.

Run the application using:

python main.py

Follow the on-screen prompts to enter your guesses.

🛠 Known Issues

The rectangle is always generated with positive coordinates; no negative coordinate cases are currently handled.

User input is not validated; entering non-numeric values may cause errors.

The turtle window may not close properly depending on the system setup.

📌 Future Improvements

Improve input validation to handle non-numeric values.

Expand coordinate ranges to include negative values for more variation.

Enhance graphical representation with better styling and colors.

Add a scoring system for better gamification.

📝 Contributing

Contributions and feedback are welcome! Feel free to submit issues or pull requests to improve the project.

📄 License

This project is open-source under the MIT License.

📢 Disclaimer

This is a simple experimental project designed for learning purposes. It may contain bugs or unintended behaviors.

