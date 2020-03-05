# Gestione delle pull requests
:warning: **DISCLAIMER** :warning: **Questo documento non si propone di essere una guida definitiva per l'uso delle pull request**

![Pull requests](https://github.com/TennersUnipd/developmentConfigurations/blob/master/GuideInterne/GitSetup.md/imgs/pullRequestExample.png)

## Come verificare che le modifiche richieste siano state effettuate

 ### 1. Verificare che le verifiche automatiche siano state eseguite correttamente


![Controlli ok](https://github.com/TennersUnipd/developmentConfigurations/blob/master/GuideInterne/GitSetup.md/imgs/checkOk.png)

Se i controlli dovessero essere ancora in corso attendere il loro completamento.
In caso di errore di esecuzione dei controlli automatici verificatene l'esito selezionando l'attività che segnala l'errore.
Fare click su dettagli, se l'errore non è relativo all'esecuzione del test ma al suo setup contattare l'amministratore.

### 2. Verifica statica delle modifiche
Ogni modifica prima di essere approvata necessita di controlli, per esser certi che le modifiche richieste siano state implementate in maniera corretta verificate con lo strumento di Review messo a disposizione da GitHub.
Per eseguire una review fare click sulla tab Files changed e verificare le modifiche fatte a ogni singolo file.

![Controlli ok](https://github.com/TennersUnipd/developmentConfigurations/blob/master/GuideInterne/GitSetup.md/imgs/filechanged.png)

E per ogni modifica effettuata verificate la differenza sulla versione precedente,una volta effettuta la verifica fate click sulla spunta di avvenuta analisi.

![Controlli ok](https://github.com/TennersUnipd/developmentConfigurations/blob/master/GuideInterne/GitSetup.md/imgs/filediff.png)