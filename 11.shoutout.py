import pyttsx3
engine=pyttsx3.init()
name=["Sanchi","Ya","Anuj","Dro"]
for i in name:
    text=f"Shoutout to {i}"
    engine.say(text)
    engine.runAndWait()