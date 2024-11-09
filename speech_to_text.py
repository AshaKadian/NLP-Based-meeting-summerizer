# Python program to translate
# speech from an audio file to text and save it to a text file

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

# Function to convert audio file to text and save it
def audio_to_text(file_path, output_file):
    try:
        # Use the audio file as the audio source
        with sr.AudioFile(file_path) as source:
            # Adjust for ambient noise and record the audio from the file
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_data = r.record(source)  # read the entire audio file

            # Using Google Speech Recognition to convert audio to text
            text = r.recognize_google(audio_data)
            text = text.lower()

            # Print and save the text
            print("Transcription: ", text)
            with open(output_file, "w") as file:
                file.write(text)

            # Optionally, you can also use text-to-speech here
            SpeakText(text)

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        
    except sr.UnknownValueError:
        print("Unable to recognize the audio")

# Example usage
audio_file_path = r"C:\Users\Nisha kadian\Documents\harvard.wav"



output_text_file = r"C:\Users\Nisha kadian\Desktop\Output\text doc output.txt"


audio_to_text(audio_file_path, output_text_file)
