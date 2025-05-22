# **[Desafio UOL HOST (Em Python)](https://github.com/uolhost/test-backEnd-Java/tree/master)**

## 📌 Sobre

***Teste para BackEnd para UOL HOST***
O teste consiste em montar uma aplicação capaz de recuperar informações de um arquivo XML e de um arquivo JSON, persistir um cadastro em um banco de dados em memória ou em arquivo e listar os cadastros em uma interface simples.

## Proposta
O 'novo' sistema de cadastro de jogadores do UOL precisa de uma nova cara! Isso porque a área de lazer da empresa definiu que todo jogador deverá ter um codinome. A proposta foi um sucesso e muitos candidatos se inscreveram, por isso a área de lazer acabou restringindo os codinomes em duas listas distintas: "Os Vingadores" e "A Liga da Justiça".

### Seu desafio é elaborar um sistema em Java capaz de:

- Permitir o cadastro de jogadores de acordo com os codinomes contidos nos links de referência vingadores.json e liga_da_justica.xml
- Apresentar um cadastro contendo nome, e-mail e telefone do jogador (sendo que nome e e-mail são obrigatórios)
- Persistir a informação cadastrada em um banco de dados em memória, como HSQLDB ou arquivo
- Obter, a qualquer momento, a lista de todos os jogadores cadastrados com seus respectivos codinomes e também a informação de qual lista o codinome foi extraído
- Impedir a utilização de um mesmo codinome para diferentes usuários (a menos que o codinome seja para listas diferentes)
- Incluir o codinome escolhido dentro das listas Os Vingadores ou A Liga da Justiça
- Obrigatoriamente, ler a informação do codinome em arquivos na internet (links abaixo). Atenção: não vale guardar a informação do codinome localmente (em um arquivo, em uma classe, em um banco de dados etc.)

### Links dos arquivos de referência

[liga_da_jutiça.xml](https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/liga_da_justica.xml)\
[vingadores.json](https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/vingadores.json)

## Casos de uso

- Cadastro com sucesso:
  - O usuário 'Felipe' cadastra seu nome, e-mail e telefone, e escolhe a lista vingadores.json
  - O sistema recebe o cadastro e verifica se há codinomes disponíveis na lista vingadores.json
  - O sistema encontra um codinome livre e o escolhe
  - O sistema persiste nome, e-mail, telefone, codinome e arquivo de referência em um banco de dados em memória ou em um arquivo
  - O sistema informa que o usuário foi cadastrado corretamente e mostra uma imagem de sucesso

- Lista escolhida não tem codinomes disponíveis:
  - O usuário 'João' cadastra seu nome, e-mail e telefone, e escolhe a lista liga_da_justica.xml
  - O sistema recebe o cadastro e verifica se há codinomes disponíveis na lista liga_da_justica.xml
  - O sistema não encontra um codinome livre
  - O sistema informa que aquela lista não possui mais usuários disponíveis

- Relatório de usuários cadastrados:
  - O usuário 'Luís' clica em “Visualizar relatório de jogadores”
  - O sistema consulta o banco de dados em memória ou em arquivo
  - O sistema apresenta todos os usuários cadastrados. Cada linha tem as informações: nome, e-mail, telefone, codinome e arquivo referência
  
## Primeiros Passos

- Inicializar Ambiente Virtual (Recomendado) (Windows)
```bash
py -m venv venv  

.\venv\Scripts\activate
```

- Instalação de Dependências
```bash
pip install django requests
```

- Iniciar Projeto (Porta)
```bash
py manage.py runserver.py
```
Após isso ele abrirá o servidor na [porta local](http://127.0.0.1:8000)