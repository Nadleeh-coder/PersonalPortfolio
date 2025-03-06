Calorie Calculator Web App

🚧 Work in Progress 🚧

This is a web-based calorie calculator built using Flask. It allows users to input their weight, height, age, and location, then retrieves the local temperature and calculates their daily calorie needs. The app features a simple web interface and displays the results dynamically.

📌 Overview

The Calorie Calculator Web App takes the following inputs:

Weight (in kg)

Height (in cm)

Age (in years)

City and country for temperature retrieval

It then computes the estimated daily calorie requirement using a basic formula and displays the results in a user-friendly format.

⚙️ Features

✅ Simple web interface using Flask.
✅ Retrieves real-time temperature based on user location.
✅ Calculates the estimated daily calorie intake.
✅ Displays the results dynamically.
✅ Easy navigation between pages.

🚀 Installation & Setup

Prerequisites

Ensure you have the following installed:

Python 3.x

Pip (Python package manager)

Flask & WTForms

Install Dependencies

Run the following command to install the required libraries:

pip install flask requests wtforms selectorlib

Run the Application

Execute the script with:

python main.py

Then, open a web browser and navigate to:

http://127.0.0.1:5000/

🛠 Known Issues

⚠ Temperature scraping depends on timeanddate.com/weather/, which may change its structure, affecting data retrieval.
⚠ No input validation for extreme values.
⚠ UI is minimal and could be improved.

📌 Future Improvements

Implement error handling for failed temperature scrapes.

Add support for different calorie calculation formulas.

Improve UI/UX with better styling and JavaScript enhancements.

Store past calculations using a database.

📝 Contributing

Contributions and feedback are welcome! Feel free to submit issues or pull requests to improve this project.

📄 License

This project is open-source under the MIT License.

📢 Disclaimer

This is an experimental project and may not work perfectly. Use at your own discretion!