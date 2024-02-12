import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import openai
import psutil

#esting the chatgpt api
api_key = 'Your api key for chatgpt'
openai.api_key=api_key

#estding the speak "male"
jarvis = pyttsx3.init()
jarvis.say("Please speake something...")
jarvis.runAndWait()

#esting the audio listener 
def convert_audio_to_text():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            #activating chatgpt
            if "activate friday" == text.lower():
                ask_gpt3()
            if "what's my battery percentage" == text.lower():
                show_battery()
            if "open chrome" in text.lower():
                open_chrome()
            if "open google" in text.lower():
                open_google()
            if "bye" in text.lower():
                jarvis.say("bye have a good day....")
                jarvis.runAndWait()
                break
        except sr.UnknownValueError:
            print("Sorry, I colud not understand what you said.")
        except sr.RequestError:
            print("Sorry, I could not request the recognition. Check your intrest connnection.")
def ask_gpt3():
    friday=pyttsx3.init()
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[1].id)  # Index 1 represents a female voice
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Friday is activated...")
            friday.say("friday is activated...")
            friday.runAndWait()
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            response = openai.Completion.create(
                engine="davinci",
                prompt=f"You: {text}\nChatGPT:",
                max_tokens=100,
                top_p=0.9,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["\n"]
            )
            chat_gpt_response = response.choices[0].text.strip()
            print(f"ChatGPT: {chat_gpt_response}")
            friday.say(chat_gpt_response)
            friday.runAndWait()

            if "bye" == text.lower():
                friday.say("bye bye sir, call me when you need me...")
                friday.runAndWait()
                break


        except sr.UnknownValueError:
            print("Sorry, I didn't understand")

def show_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    print(f"sir, your battery is {percent} percentage")
    jarvis.say(f"sir, your battery is {percent} percentage")   
    jarvis.runAndWait()

def open_google():
    jarvis.say("Opening Google")
    jarvis.runAndWait()
    webbrowser.open("https://www.google.com")

def open_chrome():
    jarvis.say("Opening Chrome...")
    jarvis.runAndWait()
    folder_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk" # Replace with the actual path
    os.system(f'explorer "{folder_path}"')
    
        



#calli8ng the audio listener function 
if __name__ == "__main__":
    convert_audio_to_text()
