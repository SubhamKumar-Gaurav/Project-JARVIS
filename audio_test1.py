import speech_recognition as sr

# List all audio input devices
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index}: {name}")

r = sr.Recognizer()
r.energy_threshold = 300  # Adjust this value as needed


# Use the correct microphone index
r = sr.Recognizer()
with sr.Microphone(device_index=5) as source:
    print("Listening...")
    audio = r.listen(source)
    print(audio) 
