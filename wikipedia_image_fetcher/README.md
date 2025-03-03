Wikipedia Image Fetcher

🚧 Work in Progress 🚧

This project is still in development, but it is functional for retrieving Wikipedia images for select queries such as moon, earth, human, and other common topics. Expect some bugs and incomplete features.

📌 Overview

This is a Python application built with Kivy that allows users to search for a topic and display the first available image from Wikipedia.

⚙️ Features

Search for a topic using a text input field

Retrieve the first image from the Wikipedia page

Display the image in the app

Download and save the image locally

🚀 Installation & Setup

Prerequisites

Make sure you have the following installed:

Python 3.x

Pip (Python package manager)

Install Dependencies

Run the following command to install the required libraries:

pip install kivy wikipedia-api requests pillow

Run the Application

python main.py

🛠 Known Issues

Some queries might return no image or the wrong image due to Wikipedia disambiguation.

The app does not yet handle multiple image selection.

Network errors are not yet fully managed.

📌 Future Improvements

Improve error handling for Wikipedia search issues.

Allow users to select from multiple available images.

Implement a more user-friendly UI.

📝 Contributing

Since this is still a work in progress, contributions and feedback are welcome! Feel free to submit issues or pull requests.

📄 License

This project is open-source under the MIT License.

📢 Disclaimer

This is an experimental project and may not work perfectly. Use at your own discretion!