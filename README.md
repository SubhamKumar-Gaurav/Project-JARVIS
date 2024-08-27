# Project-JARVIS
# Jarvis Virtual Assistant

Jarvis is a Python-based virtual assistant that can perform a variety of tasks through voice commands, including searching Wikipedia, opening websites, playing music, and telling the current time.

## Features

- **Voice Recognition**: Jarvis listens to your commands through your microphone and converts your speech to text using the `speech_recognition` library.
- **Text-to-Speech**: Jarvis responds with voice feedback using the `pyttsx3` library.
- **Wikipedia Search**: Search for topics on Wikipedia and get a brief summary.
- **Open Websites**: Quickly open popular websites like YouTube, Google, and GitHub.
- **Play Music**: Play music from a specified directory on your computer.
- **Tell Time**: Jarvis can tell you the current time.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YourUsername/Jarvis-Virtual-Assistant.git
    cd Jarvis-Virtual-Assistant
    ```

2. **Install the required dependencies**:
    ```bash
    pip install pyttsx3 speechrecognition wikipedia
    ```

3. **Ensure you have the following additional setups**:
    - For `pyttsx3` to work properly, ensure you have `sapi5` voices installed on your Windows machine.
    - If you encounter issues with `speech_recognition`, ensure that the `PyAudio` library is installed correctly.

## Usage

1. **Run the script**:
    ```bash
    python jarvis.py
    ```

2. **Give commands to Jarvis**:
    - Say "search Wikipedia for [topic]" to search for a topic on Wikipedia.
    - Say "open YouTube" to open YouTube in your default web browser.
    - Say "open Google" to open Google.
    - Say "open GitHub" to open GitHub.
    - Say "play music" to play a song from your specified music directory.
    - Say "what is the time" to have Jarvis tell you the current time.

## Customization

- **Change Voice**: You can change the voice Jarvis uses by modifying the `voices` index in the script:
    ```python
    engine.setProperty('voice', voices[0].id)  # Change 0 to 1 for a female voice
    ```
- **Music Directory**: Update the `music_dir` variable to point to your preferred music folder:
    ```python
    music_dir = 'C:\\Path\\To\\Your\\Music\\Folder'
    ```

## Troubleshooting

- **PyAudio Issues**: If you encounter issues related to `PyAudio`, ensure that you have installed the correct version of `PyAudio` compatible with your Python version.
- **Speech Recognition Issues**: If Jarvis isn't recognizing your voice, try adjusting the `energy_threshold` or check your microphone settings.

## Contributing

Contributions are welcome! If you have ideas for improving Jarvis or want to add new features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [Wikipedia API](https://pypi.org/project/wikipedia/) 
