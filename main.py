import pyttsx3

def main():
    chosen_voice = input("Voices:\n1.Microsoft Zira Desktop - English (United States)\n"
                         "2.Microsoft David Desktop - English (United States)\n"
                         "3.Bdl\n4.Clb\n5.Slt\n"
                         "Choose a voice: ")
    text = input("Enter any text: ")

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        if voice.name == chosen_voice:
            engine.setProperty('voice', voice.id)

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
