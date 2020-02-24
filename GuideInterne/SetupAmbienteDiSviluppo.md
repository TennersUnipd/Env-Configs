# Guida per il setup dell'ambiente di sviluppo

## Node.js & npm

### GNU/Linux
Per l'installazione di Node.js in una distro linux bisogna fare riferimento al proprio package manager e preferire l'installazione della versione lts.
npm verrà installato come dipendenza di Node.js.

### Windows e MacOS
Per entrambi sistemi operativi è possibile scaricare Node.js con npm direttamente dal sito di [riferimento](https://nodejs.org/it/). L'installazione di default dovrebbe essere sufficiente.

## [Visual Studio Code](https://code.visualstudio.com/)

Sulla pagina sono presenti link per l'installazione su tutti i sistemi operativi.

## Truffle & Ganache-cli
``` npm install truffle ganache-cli -g```
non è necessario scaricare ed installare il compilatore di solidity perché truffle scarica il compilatore adeguato.

## TypeScript, Mocha & Chai
```npm install typescript mocha chai -g```

## I plugin raccomandati per Visual Studio Code
[Solidity support](https://marketplace.visualstudio.com/items?itemName=JuanBlanco.solidity)
[ESLint Support](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)