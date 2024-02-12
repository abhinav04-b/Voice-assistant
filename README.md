# Voice-assistant
Backend for a voice integrated assistant with chat gpt and python.
Friday is a Python-based conversational AI assistant designed to interact with you through voice commands and provide helpful information and actions.

Features:

Speech Recognition: Utilizes speech_recognition to convert your spoken commands into text.

ChatGPT Integration: Leverages OpenAI's API to access the powerful ChatGPT 3 model for more complex language understanding and responses.

Basic Voice Assistant Features: Responds to prompts like "open chrome," "open google," "what's my battery percentage," and provides relevant information.

Customizable Voice (Male/Female): Allows you to choose the voice type for Friday using pyttsx3.
Setup:

Install required libraries: pip install speech_recognition, webbrowser, os, pyttsx3, openai

Replace "Your api key for chatgpt" with your own OpenAI API key.

Adjust the folder_path variable in open_chrome() to match your Chrome shortcut location.

Run the script: python main.py

Code Overview:

Python
# Import libraries

...

# Initialize ChatGPT API

...

# Initialize voice assistant (Jarvis)

...

def convert_audio_to_text():
    # ... Audio recognition and command handling

def ask_gpt3():
    # ... Activate Friday, listen for commands, interact with ChatGPT

def show_battery():
    # ... Get battery level, speak using Jarvis

def open_google():
    # ... Speak confirmation, open Google Chrome

def open_chrome():
    # ... Speak confirmation, open Chrome based on path

if __name__ == "__main__":
    convert_audio_to_text()
