# !pip install https://huggingface.co/bullmount/it_nerIta_trf/resolve/main/it_nerIta_trf-any-py3-none-any.whl

# Using spacy.load().
import spacy
nlp = spacy.load("it_nerIta_trf")

# # Importing as module.
# import it_nerIta_trf
# nlp = it_nerIta_trf.load()

doc = nlp('''

[00:00:00] Bot:  Buongiorno sono futura, come posso aiutarla?
[00:00:09] User:  S� io ho problemi con il mio internet banking
[00:00:09] Bot:  Se ha problemi di accesso mi dia un attimo per controllare lo stato della sua linea.
[00:00:15] Bot:  Per favore pronunci il suo nome e cognome
[00:00:23] User:  Stefano ingrosso
[00:00:23] Bot:  Piacere signor Stefano ingrosso, sto controllando lo stato della sua linea
[00:00:29] Bot:  Sembra che sia necessario resettare la password
[00:00:33] Bot:  Per cambiare password, dica "s� desidero cambiare la password" Altrimenti dica "no, interrompi"
[00:00:47] User:  S� desidero cambiare la password
[00:00:47] Bot:  Procedo con l'identificazione
[00:00:50] Bot:  Pronunci la sua data di nascita
[00:00:58] User:  3 novembre del 95
[00:00:58] Bot:  Le abbiamo appena inviato un messaggio sul suo cellulare, pronunci il codice
[00:01:12] User:  23 23
[00:01:12] Bot:  Le abbiamo appena inviato una nuova password temporanea per accedere al servizio.
[00:01:34] Bot:  Al primo accesso, le verr� richiesto di cambiarla. C'� altro che posso fare per lei?
[00:01:49] User:  S� io ho urgenza Non sono soddisfatto del vostro servizio Ho bisogno di un appuntamento
[00:01:49] Bot:  Gentile signore,quando desidera fissare un appuntamento col suo gestore?
[00:02:03] User:  � una cosa urgente Quindi domani mattina alle 10
[00:02:03] Bot:  Se il suo gestore alle 10 � libero, fisso un appuntamento a suo nome.  C'� altro che posso fare per lei?
[00:02:19] User:  No no va bene cos� Va bene cos� grazie
[00:02:19] Bot:  Allora la saluto
[00:02:21] Bot:  Ciao e buona giornata

''')

# Iterate over the entities and print their label and text
for ent in doc.ents:
    print(ent.label_, ent.text)