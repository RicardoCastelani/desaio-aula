import csv

class AgendaHeroes:

    def __init__(self):
        self.tabela = []
        for i in range(26):
            self.tabela.append([])

    def adicionar_contato(self, nome, telefone,):
        posicao = ord(nome[0]) - ord('A')
        lista = self.tabela[posicao]
        lista.append((nome, telefone,))

    def buscar_contato(self, nome):
        posicao = ord(nome[0]) - ord('A')
        lista = self.tabela[posicao]
        for contato in lista:
            if contato[0] == nome:
                return contato
        return None

    def listar_contatos(self, letra):
        posicao = ord(letra) - ord('A')
        lista = self.tabela[posicao]
        for contato in lista:
            print(contato)

    def remover_contato(self, nome):
        posicao = ord(nome[0]) - ord('A')
        lista = self.tabela[posicao]
        for i, contato in enumerate(lista):
            if contato[0] == nome:
                del lista[i]
                return True
        return False

def carregar_contatos(agenda, arquivo):
    with open(arquivo, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for linha in reader:
            nome = linha[0]
            telefone = linha[1]
            agenda.adicionar_contato(nome, telefone,)

def menu():
    agenda = AgendaHeroes()
    carregar_contatos(agenda, 'agenda.csv')
    while True:
        print('1. Adicionar contato')
        print('2. Buscar contato')
        print('3. Listar contatos')
        print('4. Remover contato')
        print('5. Sair')
        opcao = input('Opção: ')
        if opcao == '1':
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            agenda.adicionar_contato(nome, telefone,)
        elif opcao == '2':
            nome = input('Nome: ')
            contato = agenda.buscar_contato(nome)
            if contato is not None:
                print(contato)
            else:
                print('Contato não encontrado.')
        elif opcao == '3':
            letra = input('Letra: ')
            agenda.listar_contatos(letra)
        elif opcao == '4':
            nome = input('Nome: ')
            if agenda.remover_contato(nome):
                print('Contato removido.')
            else:
                print('Contato não encontrado.')
        elif opcao == '5':
            break

menu()

