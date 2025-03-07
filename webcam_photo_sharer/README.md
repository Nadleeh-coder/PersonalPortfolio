Webcam Photo Sharer

🚧 Work in Progress 🚧

Webcam Photo Sharer is a simple application that allows users to capture photos using their computer's webcam, upload them to the web, and generate a shareable link.

📌 Overview

This app enables users to:

Start and stop their computer's webcam.

Capture a photo and save it locally.

Upload the photo to the web.

Generate and copy a shareable link for easy sharing.

⚙️ Features

✅ Start and stop webcam functionality.
✅ Capture and save images locally.
✅ Upload images to the web using FileStack.
✅ Generate a shareable link for each captured image.
✅ Copy the link to the clipboard.
✅ Open the link in a web browser.

🚀 Installation & Setup

Prerequisites

Ensure you have the following installed:

Python 3.x

Pip (Python package manager)

Kivy (for GUI functionality)

Filestack Python SDK

Install Dependencies

Run the following command to install the required libraries:

pip install kivy filestack

FileStack API Key

You need to supply your own FileStack API key to use the upload functionality. Replace the default API key in filesharer.py with your own.

def __init__(self, filepath, api_key=""):
      self.filepath = filepath
      self.api_key = api_key

Run the Application

Execute the script with:

python main.py

🛠 Known Issues

⚠ The app currently does not support video recording.
⚠ No error handling for missing API keys.
⚠ Requires an active internet connection for uploading photos.

📌 Future Improvements

Add a video recording feature.

Improve UI/UX design.

Implement error handling for better user experience.

Support different image formats.

📝 Contributing

Contributions and feedback are welcome! Feel free to submit issues or pull requests to improve this project.

📄 License

This project is open-source under the MIT License.

📢 Disclaimer

This is an experimental project and may not work perfectly. Use at your own discretion!

