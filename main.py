import pyttsx3
engine = pyttsx3.init()

# eine while True oder for ... schleife Text len === text len stop 
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-70)
engine.say("hallo ich bin mimuk von pipi kakaland habe pipi gemacht,das wetter ist sehr schön ich gehe gleich zu schule habe pipi kacka gemacht in pipikakaland")
engine.runAndWait()
