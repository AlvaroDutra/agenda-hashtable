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
                    print(f"O nome está no Index {index}")
                    return True
        print("O nome não foi encontrado")
        return False

    def display(self):
        for i, slot in enumerate(self.table):
            print(f"Index {i}: {slot}")

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, slot in enumerate(self.table[index]):
                if slot[0] == key:
                    self.table[index].pop(i)
                    return True
            return False

class Contato:
    def __init__(self, nome, telefone, grau):
        self.nome = str(nome)
        self.telefone = int(telefone)
        self.grau = str(grau)

        match self.grau:
            case "1":
                grau = "Profissional"
            case "2":
                grau = "Amigo"
            case "3":
                grau = "Colega"
            case "4":
                grau = "Parceiro"
            case "5":
                grau = "Parente"
            case "6":
                grau = input("Insira o grau de proximidade do contato: ")

    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Grau: {self.grau}")

tabelahash = HashTable(10)

class PhoneBook:
    def add_contact(self):
        nome = input("Insira o nome do contato a ser adicionado: ")
        telefone = input("Insira o telefone do contato a ser adicionado: ")
        grau = input("Insira o grau do contato a ser adicionado: \n 1: Profissional \n 2: Amigo \n 3: Colega \n 4: Parceiro \n 5: Parente \n 6: Outro \n")
        tabelahash.insert(Contato(nome, telefone, grau))
        tabelahash.display()

    def get_contact(self):
        nome = input("Insira o nome do contato a ser buscado: ")
        tabelahash.search(nome)

    def remove_contact(self):
        nome = input("Insira o nome do contato a ser removido: ")
        tabelahash.delete(nome)
        tabelahash.display()

if __name__ == '__main__':
    print("AGENDA")
    while True:
        nav = int(input(" 1. ADICIONAR CONTATO \n 2. BUSCAR CONTATO \n 3. REMOVER CONTATO \n 4. EXIBIR CONTATOS \n 5. PRIORIZAR CONTATO \n 6. BLOQUEAR CONTATO \n"))
        agenda = PhoneBook()

        match nav:
            case 1:
                agenda.add_contact()
            case 2:
                agenda.get_contact()
            case 3:
                agenda.remove_contact()