from email import message
from email.mime import audio
from neuralintents import GenericAssistant
import speech_recognition
import sys
from gtts import gTTS
from playsound import playsound
import os

import time


import keyboard
import sys


def kb():
    while True:
        if keyboard.is_pressed("a"):
            print("A key was pressed")
            quit()




counter = 1
# create and open a new file named differently from the previous
def uniquify(path):
    global counter
    filename, extension = os.path.splitext(path)
    # counter = 1

    while os.path.exists(path):
        path = filename + "_" + str(counter)  + extension
        counter += 1

    return path

# open a (new) file to write
call_to_text = open(uniquify("transcriptions/tr.txt"), "w")
db_csv = open("transcriptions/database.csv", 'a', newline='')
# infos_keys = [Index, Name, DoB, change_pw, block_card, timetables, appointment, login_issue,card_enable, change_residence_data, claim_report, card_services_purchase
# ]
infos = [0]*12
infos[0] = counter - 1 
infos[1] = 'Unknown'
infos[2] = 'Unknown'

def speak(text):
    global infos, t
    
    t1 = time.strftime("%H:%M:%S", time.gmtime(int(time.time()- t)))

    call_to_text.write(f'[{t1}] Bot:  {text}')
    call_to_text.write("\n")
    tts =gTTS(text=text,lang='it')
    filename = "voce.mp3"
    if os.path.exists(filename):
        os.remove(filename)

    tts.save(filename)
    playsound(filename)
    os.remove(filename)
    
recognizer = speech_recognition.Recognizer()

def hello():
    speak('Ciao, come posso aiutarti?')
    

def quit():
    global infos
    speak('Ciao e buona giornata')
    db_csv.write(f'{str(infos)[1:-1]}\n')
    call_to_text.close()
    sys.exit(0)

def change_pw():
    global infos, recognizer, t
    speak('Per cambiare password, dica "sì desidero cambiare la password" Altrimenti dica "no, interrompi"')
    # speak('Altrimenti dica "no, interrompi"')
    done = False

    while not done:
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                func_start = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))
                call_to_text.write(f'[{curr_t}] User:  {func_start}')
                call_to_text.write("\n")
            
                
                matches = ["desider", "cambiare", "password"]

                if any(x in func_start for x in matches):
                    speak("Procedo con l'identificazione")
                    done = True
                else:
                    speak("Ho interrotto il cambio, c'è altro che posso fare per lei?")
                    return
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, può ripetere?')

    done = False
    speak('Pronunci nome cognome')
    while not done:
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                id_name = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))
                call_to_text.write(f'[{curr_t}] User:  {id_name}')
                call_to_text.write("\n")
                                
                done = True
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, mi dispiace')
    
    done = False
    speak('Pronunci la sua data di nascita')
    while not done:
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                dob = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))
                call_to_text.write(f'[{curr_t}] User:  {dob}')
                call_to_text.write("\n")
                infos[2] = dob
                      
                done = True
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, mi dispiace')
    
    #TO-DO: cerco nel data-base il num di telefono

    done = False
    speak('Le abbiamo appena inviato un messaggio sul suo cellulare, pronunci il codice')
    while not done:
        # time.sleep(2)
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                tmp_code = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))
                call_to_text.write(f'[{curr_t}] User:  {tmp_code}')
                call_to_text.write("\n")

                #TO-DO: controllare che il codice sia corretto
                infos[3] = 1
                speak('Le abbiamo appena inviato una nuova password temporanea per accedere al servizio.')
                speak("Al primo accesso, le verrà richiesto di cambiarla. C'è altro che posso fare per lei?")
                done = True
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, può ripetere?')

def block_card():
    global infos, recognizer, t
    speak('Se desidera bloccare la sua carta pronunci la sua data di nascita')

    done = False

    while not done:
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                id_code = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))
                call_to_text.write(f'[{curr_t}] User:  {id_code}')
                call_to_text.write("\n")
                
                #TO-DO: inviare nuova password con codice id_code
                infos[4] = 1

                speak("Abbiamo provveduto a bloccare la sua carta e ad emetterne una nuova, che verrà spedita alla sua filiale di riferimento. C'è altro che posso fare per lei?")
                done = True
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, mi dispiace')


def appointment():
    global infos, recognizer, t
    speak('Prima di fissare un appuntamento ci dica il suo nome e cognome per indirizzarla al suo gestore')

    done = False

    while not done:
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                
                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                id_name = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))

                call_to_text.write(f'[{curr_t}] User:  {id_name}')
                call_to_text.write("\n")
                
                infos[1] = id_name
                #TO-DO: inviare nuova password con codice id_code
                
                speak('Piacere signor ' + id_name  + ',quando desidera fissare un appuntamento col suo gestore?')
                done = True
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, mi dispiace. Può ripetere?')
    
    done = False
    while not done:
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                timetable = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))
                call_to_text.write(f'[{curr_t}] User:  {timetable}')
                call_to_text.write("\n")
                timetable = ''.join(c for c in timetable if c.isdigit())
                ans = "Se il suo gestore alle " + timetable + " è libero, fisso un appuntamento a suo nome.  C'è altro che posso fare per lei?"
                speak(ans)
                infos[5] = 1
                done = True
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, mi dispiace')

def login_issue():
    global infos, recognizer, t
    speak('Se ha problemi di accesso mi dia un attimo per controllare lo stato della sua linea.')
    speak('Per favore pronunci il suo nome e cognome')
    
    done = False

    while not done:
        try:
            with speech_recognition.Microphone(device_index=1) as mic:

                
                recognizer.adjust_for_ambient_noise(mic, duration=0.05)
                audio = recognizer.listen(mic)
                id_name = recognizer.recognize_google(audio, language="it-IT")
                curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))

                call_to_text.write(f'[{curr_t}] User:  {id_name}')
                call_to_text.write("\n")
                infos[1] = id_name

                #TO-DO: inviare nuova password con codice id_code
                
                speak('Piacere signor ' + id_name  + ', sto controllando lo stato della sua linea')
                done = True
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speak('Non ho capito, mi dispiace. Può ripetere?')

    #TO-DO: elaborazione della richiesta --> è necessario cambiare la password
    infos[7] = 1
    speak('Sembra che sia necessario resettare la password')
    change_pw()

def card_services_purchase():
    global infos
    infos[10] = 1
    speak("Per acquistare un servizio seguire le procedure. C'è altro che posso fare per lei?")

def claim_report():
    global infos
    infos[9] = 1
    speak("Per denunciare un sinistro seguire le procedure. C'è altro che posso fare per lei?")

def change_residence_data():
    global infos
    infos[8] = 1
    speak("Per cambiare i dati sulla residenza seguire le procedure. C'è altro che posso fare per lei?")

def card_enable():
    global infos
    infos[7] = 1
    speak("Per attivare la carta seguire le procedure. C'è altro che posso fare per lei?")


def timetables():
    global infos
    infos[4] = 1
    speak("La banca è aperta dal lunedì al venerdì dalle 8:20 alle 19:20. C'è altro che posso fare per lei?")

def none():
    global infos
    infos[11] = 1
    speak("Non sono in grado di aiutarti, chiedimi qualcosa a cui posso rispondere")


def job_ended ():
    speak("Allora la saluto")
    quit()

mappings = {
    'card_services_purchase': card_services_purchase,
    'claim_report': claim_report,
    'change_residence_data': change_residence_data,
    'card_enable': card_enable,
    'login_issue': login_issue,
    'appointment': appointment,
    'timetables': timetables,
    'block_card':block_card,
    'change_pw': change_pw,
    
    'exit' : quit,
    'job_ended': job_ended,
    'none': none,
    }


assistant = GenericAssistant('intents_gtts.json', intent_methods=mappings)
assistant.train_model()

# assistant.request("")

# for manually deciding when to start the call
input = input()

t = time.time()
speak('Buongiorno sono futura, come posso aiutarla?')

while True:
    try:
        
        with speech_recognition.Microphone(device_index=1) as mic:
            
            if keyboard.is_pressed('q'):
                quit()

            recognizer.adjust_for_ambient_noise(mic, duration=0.05)
            audio = recognizer.listen(mic)
            # print(type(audio))
            
            message = recognizer.recognize_google(audio, language="it-IT")
            curr_t = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - t)))
            call_to_text.write(f'[{curr_t}] User:  {message}')
            call_to_text.write("\n")

            message = message.lower()
            print(message)

        assistant.request(message)

    except speech_recognition.UnknownValueError:
        time.sleep(3)
        speak("Se ha detto qualcosa non l'ho sentita, puo' ripetere?")
        recognizer = speech_recognition.Recognizer()

