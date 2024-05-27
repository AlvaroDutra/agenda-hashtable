# **Agenda-HashTable**

Sistema de agenda telefônica feito em *Python* com fim de trabalhar a implementação e uso de uma tabela hash e entender o funcionamento de uma função hash.  

## **Grupo**

**Turma:** TAD - 3º semestre - Estrutura de Dados

* [Álvaro Gabriel Nadaleti Dutra](https://github.com/AlvaroDutra)
* [Fabrício Costa Fernandes Filho](https://github.com/fabriciocosta77)
* [João Guilherme dos Santos](https://github.com/JoaoGuilherme2909)  

## **Funcionamento**

### Arquivo

Esse projeto possui apenas um aquivo que contém todo o código [main.py](https://github.com/fabriciocosta77/agenda-hashtable/blob/main/main.py). Apenas baixe o arquivo e abra no editor de código que preferir.

### Classes e Metodos

Esse projeto possui as seguintes classes:

1. ***HashTable***
2. ***Contato***
3. ***PhoneBook***

#### ***HashTable***

Classe que instancia uma tabela Hash. Nela possui os metodos:  

* ***Inicializador*** : Define o tamanho da tabela na hora de sua instanciação.

* ***Hash_function*** : Gera através de uma chave fornecida um índice.

* ***Insert*** : Recebe uma chave e um valor e insere na tabela utilizando um índice geredo pelo metodo hash.

* ***Search*** : Recebe uma chave como parametro e usando o índice gerado pela função hash verifica se o valor no índice não está vazio.

* ***Display*** : Mostra todos os contatos, menos os bloqueados.

* ***Display_prio*** : Mostra apenas os contatos priorizados.

* ***Display_block*** : Mostra apenas os contatos bloqueados.

* ***Delete*** : Deleta os contato que estiver no índice gerado, trocando seu valor para *None*

* ***Priorize*** : Prioriza os contatos desejaveis, colocando "⭐" no seu nome.

* ***Block*** : Bloqueia contatos desejaveis, colocando "🚫" no seu nome.

#### ***Contato***

Classe que intancia um objeto Contato. Possui apenas um metodo:

* ***Inicializador*** : Define o nome, telfone e grau do contato.

#### ***PhoneBook***

Classe onde chama metodos para criar a agenda telefônica. Possui os metodos:  

* ***Add_contact*** : Instancia um objeto *Contato* e o insere na tabela usando o metodo ***Insert***.

* ***Get_contact*** : Chama o metodo ***Search*** para o contato desejado.

* ***Remove_contact*** : Chama o metodo ***Delete*** para o contato desejado.

* ***Display_contacts*** : Chama o metodo ***Display***.

* ***Display_contacts_prio*** : Chama o metodo ***Display_prio***.

* ***Display_contacts_block*** : Chama o metodo ***Display_block***.

* ***Priorize_contact*** : Chama o metodo ***Priorize*** para o contato desejado.

* ***Block_contact*** : Chama o metodo ***Block*** para o contato desejado.
