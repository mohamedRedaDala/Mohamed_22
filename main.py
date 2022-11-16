import PyPDF2
import pyttsx3
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = pdfreader.numPages


for num in range (0,pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    #player.save_to_file(text, 'audiobook.mp3')
    player.runAndWait()