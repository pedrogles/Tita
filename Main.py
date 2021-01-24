import speech_recognition as sr

def reconhece():
     rec = sr.Recognize()
       with sr.Microphone() as s:
         rec.adjust_for_ambient_noise(s)

          while True:
          audio = rec.listen(s)

          entrada = rec.recogize_google_(audio, Lenguage="pt")
           return "Você disse {}".format(entrada)


fala = reconhece()
print(fala)
