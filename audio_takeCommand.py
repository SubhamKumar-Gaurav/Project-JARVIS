import speech_recognition as sr

r = sr.Recognizer()
def takeCommand() :
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"You said: {text}")
    except Exception as e:
        print(f"Error: {e}")

takeCommand()        