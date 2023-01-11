#generatore di insulti casuali
#generatore di insulti casuali v1.4
#creato da PERA(Marco Perazzolo)
#copyright 2023
#questo generatore casuale è in grado di generare piu' di 59560 insulti al secondo.
#cose aggiunte:
#     1.4:cronometro che segna il tempo impiegato e numero di insulti stampati


import random as r
import time as c


insulti= ['autistico','balcanico','cojone','degenere','emicranico','frocio','gay','hijo de puta','i pomodorini sopra la bruschetta','juventino','kitemmuort','lercio','Mona con la M maiuscola','negro','obeso','puttan*','quaqquaraqua','rincoglionito','stronzo','trimone','uzbeco','venco','walter white','xilofono','yodelalahihi','zio strambuso','merdoso','terrone','incivile','canaglia','malandrino','furfantello','diversamente intelligente,a tratti balbuziente','deficente','bastardo','pagliaccio','clown popi popi','comunista','rompiballe','figlio di puttana','testa di cazzo','screanzato','lazzarone','filibustiere','pusillanime','lestofante','farabutto','villano','mezzasega','cesso','idiota','imbecille','cretino','staresti bene di fianco al bue nel presepe','quando inauguri il cervello fammelo sapere che ti regalo una pianta','sei utile come una forchetta nel brodo','hai la faccia giusta per lavorare nella pubblicità dell Imodium','il cervello è larma piu potente che esista, tu sei pacifista vero?','mi piacciono le piccole cose ma col tuo cervello si esagera','per il tuo prossimo compleanno ti regalerò un cervello nuovo incartato in un coriandolo','le tue pause di riflessione sono la parte piu interessante dei tuoi discorsi','prima di conoscerti ero sull’orlo del precipizio, ora che ti ho conosciuto penso che farò un passo avanti','ho appena saputo della tua malattia, spero non sia niente di banale','ama la natura nonostante ciò che ti ha fatto','non cè nulla di male in te che la reincarnazione non possa sistemare','devo dire che senza la tavoletta e la catenella non ti avevo riconosciuto']
a = 0


while a<9999999999:
#chiede se si vuole insulti
    p=input('vuoi insulti?(si/no)')
    if p == 'si':
#chiede il numero desiderato di insulti
            n = int(input('quanti insulti vuoi? '))
            t1=c.time()
            for f in range(n):
               print(r.choice(insulti))
            t2=c.time()
            print('dati',f+1,'insulti in',t2 - t1,'secondi')
    if p == 'no':
            print('vaffanculo')
            exit()
