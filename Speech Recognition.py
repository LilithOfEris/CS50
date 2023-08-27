import SpeechRecognition as sr
import pyttsx3

def main():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            
            if "hello" in text.lower():
                engine.say("Hello! How can I assist you?")
                engine.runAndWait()
            else:
                engine.say("I'm here, but I didn't catch that.")
                engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand audio.")
        except sr.RequestError as e:
            print("Sorry, there was an error connecting to Google's servers.")

if __name__ == "__main__":
    main()
