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
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for valor in self.table[index]:
                if valor[0] == key:
                    print(f"O contato {key} está no Índice {index}")
                    print(f"O número do contato {key}: {valor[1][0]} \nO grau de proximidade do contato {key}: {valor[1][1]} ")
                    continuar = input("Aperte qualquer tecla para voltar...")
                    if continuar is not None:
                        continue
                    return True
        print(f"O contato {key} não existe")
        return False

    def display(self):
        # Mostra todos os contatos menos os bloqueados
        for i, slot in enumerate(self.table):
            if slot is not None:
                if "🚫" in slot:
                    pass
                else:
                    for valor in self.table[i]:
                        print(
                            f"O nome do contato no índice {i} é {valor[0]} \n"
                            f"O número do contato no índice {i} é {valor[1][0]} \n"
                            f"O grau de proximidade do contato no índice {i} é {valor[1][1]} \n")

    def display_prio(self):
        # Mostra apenas os contatos priorizados
        for i, slot in enumerate(self.table):
            if slot is not None:
                if "⭐" not in slot:
                    pass
                else:
                    for valor in self.table[i]:
                        print(
                            f"O nome do contato no índice {i} é {valor[0]} \n"
                            f"O número do contato no índice {i} é {valor[1][0]} \n"
                            f"O grau de proximidade do contato no índice {i} é {valor[1][1]} \n")

    def display_block(self):
        # Mostra apenas os contatos bloqueados
        for i, slot in enumerate(self.table):
            if slot is not None:
                if "🚫" not in slot:
                    pass
                else:
                    for valor in self.table[i]:
                        print(
                            f"O nome do contato no índice {i} é {valor[0]} \n"
                            f"O número do contato no índice {i} é {valor[1][0]} \n"
                            f"O grau de proximidade do contato no índice {i} é {valor[1][1]} \n")

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, slot in enumerate(self.table[index]):
                if slot[0] == key:
                    self.table[index].pop(i)
                    return True
            return False

    def priorize(self, key):
        index = self.hash_function(key)
        self.table[index].append("⭐")

    def block(self, key):
        index = self.hash_function(key)
        self.table[index].append("🚫")

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
    tabelahash = HashTable(100)
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