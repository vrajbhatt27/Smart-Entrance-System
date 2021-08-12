import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 115)
engine.say('Hello sir, how are you')
engine.runAndWait()

