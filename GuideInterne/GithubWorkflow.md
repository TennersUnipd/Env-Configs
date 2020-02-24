# Gestione del repository
Per poter operare correttamente sul repository è necessaria la presenza di git-flow o un software di gestione grafica del repository compatibile.

# :warning: per creare correttamente un nuovo branch bisogna partite dal branch develop :warning:

```bash
git checkout develop
```

## Gestione delle aggiunte
Quando si vuole operare un task di aggiunta, bisogna creare un feature branch attraverso git flow con nome la issue di rifermento compresa di numero.

```bash
git flow feature start IssueDiRiferimento#00.
```

## Gestione delle correzioni
Quando si opera su un task che è focalizzato sulla correzione si crea un bugfix branch con git flow con nome la issue di rifermento compresa di numero.

```bash
git flow bugfix start IssueDiRiferimento#00.
```

### NB
Per le correzioni da fare in blocco non è necessario creare tanti branch differenti, ma ne basta uno con nome la issue di rifermento compresa di numero.
Quindi per ogni issue corrisponde un unico branch.

## Richiesta di verifica delle modifiche
Una volta concluso un task per richiederne la revisione e l'approvazione bisogna fare dall'interfaccia di GitHub una pull request sul ramo develop.
Si può creare una pull request se tutti i test automatici sono terminati con esito positivo.

Per ulteriori chiarimeti non esitate a chiedere.