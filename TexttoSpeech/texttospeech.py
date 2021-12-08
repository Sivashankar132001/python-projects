from gtts import gTTS
import os 

text = "Soothhe Koḻuppu"

#to read from file

# filesys = open('sample.txt')
# text = filesys.read()

language = "en"
obj = gTTS(text = text,lang= language, slow = True)

obj.save('sample.mp3')
os.system("sample.mp3")
