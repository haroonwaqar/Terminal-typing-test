🧑‍💻 Terminal Typing Test

Terminal Typing Test is a Python-based command-line application that helps you test and improve your typing speed. It measures your Words Per Minute (WPM) as you type a randomly selected paragraph from a text file, all within a clean terminal interface using the curses library.

💡 Features

🧾 Randomly selects a paragraph from a text file
⚡ Real-time WPM (Words Per Minute) calculation
🖥️ Clean, interactive terminal interface using curses
📚 Easy to customize text sources

🛠️ Requirements

Python 3
Install Required Library:
pip install windows-curses  # Only for Windows users
curses is built-in for Linux and macOS. Windows users need windows-curses.

🚀 How to Run

Clone the repository:
git clone https://github.com/your-username/terminal-typing-test.git
cd terminal-typing-test
Add a text.txt file containing multiple paragraphs (one per line) for the typing test.
Example:

The quick brown fox jumps over the lazy dog.
Typing fast takes practice and patience.
Python is a powerful programming language.

Run the application:
python typing_test.py

🖋️ How It Works

The app randomly selects a line from texts.txt.
You are prompted to type it as quickly and accurately as possible.
After you finish, it calculates your typing speed in WPM and shows your result.
