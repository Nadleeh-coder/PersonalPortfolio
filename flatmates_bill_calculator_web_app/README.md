Flatmates Bill Web App

🚧 Work in Progress 🚧

This is a web-based version of the Flatmates Bill Calculator, built using Flask. It allows two flatmates to input their stay duration and total bill amount, then calculates their respective shares. The app features a simple web interface and displays the results dynamically.

📌 Overview

The Flatmates Bill Web App takes the following inputs:

The total bill amount.

The billing period.

The number of days each flatmate stayed in the flat.

It then computes how much each person has to pay and displays the results in a user-friendly format.

⚙️ Features

✅ Simple web interface using Flask.
✅ Calculates each flatmate's fair share of the bill.
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

pip install flask wtforms

Run the Application

Execute the script with:

python main.py

Then, open a web browser and navigate to:

http://127.0.0.1:5000/

🛠 Known Issues

⚠ The app currently only supports two flatmates.
⚠ There is no database storage for past calculations.
⚠ Error handling for incorrect user inputs is minimal.

📌 Future Improvements

Extend support for more than two flatmates.

Add a feature to generate PDF reports like the CLI version.

Improve UI/UX with better styling and JavaScript enhancements.

Store past calculations using a database.

📝 Contributing

Contributions and feedback are welcome! Feel free to submit issues or pull requests to improve this project.

📄 License

This project is open-source under the MIT License.

📢 Disclaimer

This is an experimental project and may not work perfectly. Use at your own discretion!