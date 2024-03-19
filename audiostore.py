import speech_recognition as sr
import pyttsx3
import os
import PyPDF2

recognize=sr.Recognizer()
speech=pyttsx3.init()
voicetype=speech.getProperty('voices')
speech.setProperty('voice',voicetype[1].id)

def readpdf():
    try:
        with open(pdfname,'rb') as pdf:
            reader=PyPDF2.PdfReader(pdf)
            total_page=len(reader.pages)
            for page in range(total_page):
                pagenum=reader.pages[page]
                read=pagenum.extract_text()
                print(read)
            for page in range(total_page):
                pagenum=reader.pages[page]
                read=pagenum.extract_text()
                speech.say(read)
                speech.runAndWait()
            pdf.close()
    except:
        speech.say('Sorry, I am not able to access pdf')
        speech.runAndWait()

def writetxt():
    try:
        with sr.Microphone() as phone:
            print('Listening...')
            audio=recognize.listen(phone,timeout=2,phrase_time_limit=2)
            text=recognize.recognize_google(audio)
            print(text)
            with open(filename,mode) as file:
                file.write(text)
                file.close()
    except:
        speech.say('Sorry, I am not able to recognize you')
        speech.runAndWait()

def readtxt():
    try:
        with open(filename,'r') as file:
            text=file.read()
            print(text)
            speech.say(text)
            speech.runAndWait()
    except:
        speech.say('Sorry, I am not able to access file')
        speech.runAndWait()

def audtotxt():
    try:
        with sr.AudioFile(audiofile) as sound:
            audio=recognize.listen(sound)
            text=recognize.recognize_google(audio)
            print(text)
            with open(filename,'w') as file:
                file.write(text)
                file.close()
    except:
        speech.say('Sorry, I am not able to fetch audio')
        speech.runAndWait()

txt='Welcome to Audio read and write file...'
print(txt)
speech.say(f'{txt} please select any option from choices')
speech.runAndWait()

print('1.Text File\n2.Pdf Reader\n3.Audio to Text')
try:
    choices=int(input('Enter your choice: '))
    if choices==1:
        print('1.Read the File\n2.Write to a File')
        choice=int(input('Enter your choice: '))
        try:
            if choice==1:
                filename=input('Enter Filename: ')
                if os.path.exists(filename):
                    readtxt()
                else:
                    speech.say('please enter existing file name...')
                    speech.runAndWait()
            elif choice==2:
                filename=input('Enter Filename: ')
                if os.path.exists(filename):
                    mode='a'
                    writetxt()
                else:
                    mode='w'
                    writetxt()
            else:
                speech.say('Please enter valid choice...')
                speech.runAndWait()
        except:
            speech.say('choice is not recognized...')
            speech.runAndWait()
    elif choices==2:
        pdfname=input('Enter Pdfname: ')
        if os.path.exists(pdfname):
            readpdf()
        else:
            speech.say('please enter existing pdf name...')
            speech.runAndWait()
    elif choices==3:
        audiofile=input('Enter Filename of Audio: ')
        filename=input('Enter Filename: ')
        if os.path.exists(audiofile):
            audtotxt()
        else:
            speech.say('please enter existing audio filename...')
            speech.runAndWait()
    else:
        speech.say('Please enter valid choice...')
        speech.runAndWait()
except:
    speech.say('choice is not recognized...')
    speech.runAndWait()