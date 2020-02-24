# Guida all'uso di git per SWE
Questa guida è per uso interno e non si prefigge di essere una guida di riferimento

Prima di tutto bisogna creare delle chiavi di riconoscimento per github.

## Installazione di git
[Guida per installare git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
la guida copre tutti i sistemi operativi principali.

## Installazione di git-flow

- ### GNU/Linux
    Per quanto riguarda le distribuzioni GNU/Linux fate riferimento al vostro package manager.
- ### Windows con git 
    Questa [guida](https://www.geeknews.it/come-installare-git-flow-su-windows-con-git-.html)
    copre l'installazione di git  e git-flow
- ### MacOs
    Questa [guida](http://macappstore.org/git-flow/) copre l'installazione di GitFlow tramite il terminale

## Creazioni delle chiavi
Per creare le chiavi di validazione è possibile proseguire in modi differenti.

- Il primo è quello di seguire questa [guida](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) in particolare la sezione riguardante alla creazione di una nuova chiave SSH.

- Il secondo metodo dipende dal fatto se utilizzate un client grafico per git o meno, ad esempi GitKraken, perché alcuni includono la possibilità di generare la chiave di riconoscimento direttamente dall'applicazione.

## Git clone, add, commit, pull, push.

Una volta completato il setup di git si può procedere con il download del progetto, per lo sviluppo di ogni componente fare riferimento ad ogni repository.

Per effettuare il download del repository eseguire il comando ``` git clone <indirizzo repository remoto>```
Una volta terminato il download inizializzare git flow con ``` git flow init``` basta seguire la procedura guidata senza modificare i valori di default.

:warning: **ATTENZIONE** :warning: **Ogni repository ha i branch master e develop protetti da commit diretti**

Per iniziare a lavorare fate riferimento alla board delle issues del relativo repository.

Fate riferimento al file GitHubWorkflow.

Per poter confermare i cambiamenti bisogna aggiungerli nell'area di stagin con il comando ``` git add <percoso/del/file/modificato>``` oppure ``` git add .``` per inserire tutti i cambiamenti della directory corrente.

Dopo di che effettuare il comando ``` git commit -m "<Commento significativo delle modifiche>"```.

Prima di inviare al repository remoto le modifiche effettuate eseguite il comando ``` git pull``` per verificare che la vostra versione locale sia aggiornata all'ultimo commit.

Una volta riallineato il repository locale con quello remoto effettuare il comando ``` git push```, in questo modo le modifiche effettuate in locale verranno inviate al server remoto di GitHub.