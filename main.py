class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        key_str = str(key)
        key_int = sum([ord(c) for c in key_str])
        A = 0.6180339887
        return int(self.size * ((key_int * A) % 1))

    def insert(self, key, *value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value), None]
        else:
            print(f"Colisão detectada no índice {index}! Contato {self.table[index][0][0]} sobrescrito.")
            self.table[index] = [(key, value), None]

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            if self.table[index][0][0] == key:
                if self.table[index][1] == "⭐":
                    print(f"Este contato é priorizado! ⭐")
                if self.table[index][1] == "🚫":
                    print(f"Este contato está bloqueado! 🚫")
                print(f"O contato {key} está no Índice {index}")
                print(f"O número do contato {key}: {self.table[index][0][1][0]} \n"
                      f"O grau de proximidade do contato {key}: {self.table[index][0][1][1]} \n")

                continuar = input("Aperte qualquer tecla para voltar... \n")
                if continuar is not None:
                    pass

        else: print(f"O contato {key} não existe \n")
        return False

    def display(self):
        # Mostra todos os contatos menos os bloqueados
        for i, slot in enumerate(self.table):
            if self.table[i] is not None:
                if "🚫" in slot:
                    pass
                else:
                    if self.table[i][1] == "⭐":
                        print(f"Este contato é priorizado! ⭐")
                    print(
                    f"Contato: {self.table[i][0][0]} \n"
                    f"Número: {self.table[i][0][1][0]} \n"
                    f"Proximidade: {self.table[i][0][1][1]} \n")

    def display_prio(self):
        # Mostra apenas os contatos priorizados
        for i, slot in enumerate(self.table):
            if slot is not None:
                if "⭐" not in slot:
                    pass
                else:
                    print(
                    f"Contato ⭐: {self.table[i][0][0]} \n"
                    f"Número: {self.table[i][0][1][0]} \n"
                    f"Proximidade: {self.table[i][0][1][1]} \n")

    def display_block(self):
        # Mostra apenas os contatos bloqueados
        for i, slot in enumerate(self.table):
            if slot is not None:
                if "🚫" not in slot:
                    pass
                else:
                    print(
                    f"Contato 🚫: {self.table[i][0][0]} \n"
                    f"Número: {self.table[i][0][1][0]} \n"
                    f"Proximidade: {self.table[i][0][1][1]} \n")

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            self.table[index] = None

    def priorize(self, key):
        despriorizar = False
        index = self.hash_function(key)
        if self.table[index] is not None:
            if self.table[index][1] != "⭐":
                self.table[index][1] = ("⭐")
                print(f"Contato {self.table[index][0][0]} priorizado.")
            else:
                while despriorizar != "Y" and despriorizar != "y" and despriorizar != "N" and despriorizar != "n":
                    despriorizar = input("Esse contato já está priorizado. Deseja despriorizá-lo? (Y/N) \n")
                    if despriorizar == "Y" or despriorizar == "y":
                        print(f"Despriorizando o contato {self.table[index][0][0]}...")
                        self.table[index][1] = None
                    elif despriorizar == "N" or despriorizar == "n":
                        print(f"Voltando...")
                    else:
                        print("Comando incorreto! Use Y/N. \n")
        else: print("O contato não existe")

    def block(self, key):
        desbloquear = False
        index = self.hash_function(key)
        if self.table[index] is not None:
            if self.table[index][1] != "🚫":
                self.table[index][1] = ("🚫")
                print(f"Contato {self.table[index][0][0]} bloqueado.")
            else:
                while desbloquear != "Y" and desbloquear != "y" and desbloquear != "N" and desbloquear != "n":
                    desbloquear = input("Esse contato já está bloqueado. Deseja desbloqueá-lo? (Y/N) \n")
                    if desbloquear == "Y" or desbloquear == "y":
                        print(f"Desbloqueando o contato {self.table[index][0][0]}... \n")
                        self.table[index][1] = None
                    elif desbloquear == "N" or desbloquear == "n":
                        print(f"Voltando...")
                    else:
                        print("Comando incorreto! Use Y/N. \n")
        else: print("O contato não existe")

class Contato:
    def __init__(self, nome, telefone, grau):
        self.nome = str(nome)
        self.telefone = str(telefone)
        self.grau = str(grau)

class PhoneBook:
    def add_contact(self):
        nome = input("Insira o nome do contato a ser adicionado: ")
        telefone = input("Insira o telefone do contato a ser adicionado: ")
        grau = input("Insira o grau do contato a ser adicionado: \n 1: Profissional \n 2: Amigo \n 3: Colega \n 4: Parceiro \n 5: Parente \n 6: Outro \n")
        novo_contato =  Contato(nome, str(telefone), str(grau))

        match novo_contato.grau:
            case "1":
                novo_contato.grau = "Profissional"
            case "2":
                novo_contato.grau = "Amigo"
            case "3":
                novo_contato.grau = "Colega"
            case "4":
                novo_contato.grau = "Parceiro"
            case "5":
                novo_contato.grau = "Parente"
            case "6":
                novo_contato.grau = input("Insira o grau de proximidade do contato: ")

        tabelahash.insert(novo_contato.nome ,novo_contato.telefone, str(novo_contato.grau))

    def get_contact(self):
        nome = input("Insira o nome do contato a ser buscado: ")
        tabelahash.search(nome)

    def remove_contact(self):
        nome = input("Insira o nome do contato a ser removido: ")
        tabelahash.delete(nome)

    def display_contacts(self):
        tabelahash.display()

    def display_contacts_prio(self):
        tabelahash.display_prio()

    def display_contacts_block(self):
        tabelahash.display_block()

    def priorize_contact(self):
        nome = input("Insira o nome do contato a ser priorizado: ")
        tabelahash.priorize(nome)

    def block_contact(self):
        nome = input("Insira o nome do contato a ser bloqueado: ")
        tabelahash.block(nome)

if __name__ == '__main__':
    print("AGENDA TABELA HASH")
    print(f"Antes de continuarmos, vamos definir o tamanho da sua agenda.")
    print(f"Isso é importante! Ela não poderá ser alterada até o programa ser reiniciado e, consequentemente, seus contatos perdidos!")
    tamanho = int(input("Escolha um número entre 25 e 2000: \n"))
    if tamanho < 25:
        print("Lista muito pequena! Definindo o tamanho como 25...")
        tamanho = 25
    elif tamanho > 2000:
        print("Lista muito grande! Definindo o tamanho como 2000...")
        tamanho = 2000
    else:
        print(f"Tamanho da tabela definido como {tamanho}.")
        tabelahash = HashTable(tamanho)

    while True:
        nav = str(input(" 1. ADICIONAR CONTATO \n 2. BUSCAR CONTATO \n 3. REMOVER CONTATO \n 4. EXIBIR CONTATOS \n 5. PRIORIZAR CONTATO \n 6. BLOQUEAR CONTATO \n 7. FECHAR AGENDA \n"))
        agenda = PhoneBook()
        match nav:
            case "1":
                agenda.add_contact()
            case "2":
                agenda.get_contact()
            case "3":
                agenda.remove_contact()
            case "4":
                nav2 = str(input("   1. EXIBIR CONTATOS COMUNS \n   2. EXIBIR CONTATOS PRIORIZADOS \n   3. EXIBIR CONTATOS BLOQUEADOS \n"))
                match nav2:
                    case "1":
                        agenda.display_contacts()
                        continuar = input("Aperte qualquer tecla para voltar...")
                        if continuar is not None:
                            continue
                    case "2":
                        agenda.display_contacts_prio()
                        continuar = input("Aperte qualquer tecla para voltar...")
                        if continuar is not None:
                            continue
                    case "3":
                        agenda.display_contacts_block()
                        continuar = input("Aperte qualquer tecla para voltar...")
                        if continuar is not None:
                            continue
                    case _:
                        print("Comando inválido! Escolha um dos comandos abaixo.")
            case "5":
                agenda.priorize_contact()
            case "6":
                agenda.block_contact()
            case "7":
                print("Fechando agenda...")
                break
            case _:
                print("Comando inválido! Escolha um dos comandos abaixo.")