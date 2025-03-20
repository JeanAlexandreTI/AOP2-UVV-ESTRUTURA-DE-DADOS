#%%
# Turma: AN3tEad
# Alunos: Jean Alexandre Cabral de Oliveira, Joao Victor Fernandes do Prado
class Nodo:
    def __init__(self, dado=None, proximoNodo=None):
        self.dado = dado
        self.proximo = proximoNodo
    
    def __repr__(self):
        return f'{self.dado}->{self.proximo}'
        
    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo


class Cliente:
    def __init__(self, nome, valorDaConta):
        self.nome = nome
        self.valorDaConta = valorDaConta

    def __repr__(self):
        return f'{self.nome}->{self.valorDaConta}'


class ListaEncadeada:
    def __init__(self):
        self.head = None
    
    def inserir(self, cliente):
        if self.head is None:
            self.head = Nodo(cliente)
        else:
            current = self.head
            while current.proximo is not None:
                current = current.proximo
            current.proximo = Nodo(cliente)
    
    def percorrer(self):
        clientes = []
        current = self.head
        while current is not None:
            clientes.append(current.dado)
            current = current.proximo
        return clientes


class FilaCircular:
    def __init__(self):
        self.fila = []
    
    def inserir(self, valor):
        self.fila.append(valor)

    def ler(self):
        if len(self.fila) == 0:
            return None
        return self.fila.pop(0)


def inserir_clientes_na_lista():
    lista = ListaEncadeada()

    valores = {
        "c1": [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],
        "c2": [1000, 900, 800, 700, 600, 500, 400, 300, 200],
        "c3": [1000, 900, 800, 700, 600, 500, 400, 300],
        "c4": [1000, 900, 800, 700, 600, 500, 400],
        "c5": [1000, 900, 800, 700, 600, 500],
        "c6": [1000, 900, 800, 700, 600],
        "c7": [1000, 900, 800, 700],
        "c8": [1000, 900, 800],
        "c9": [1000, 900],
        "c10": [1000]
    }
    
    clientes = []
    for nome, contas in valores.items():
        for valor in contas:
            cliente = Cliente(nome, valor)
            lista.inserir(cliente)
            clientes.append(cliente)
    
    return lista, clientes


def calcular_media(lista):
    clientes = lista.percorrer()
    medias = {}
    
    for cliente in clientes:
        if cliente.nome not in medias:
            medias[cliente.nome] = []
        medias[cliente.nome].append(cliente.valorDaConta)

    medias_finais = []
    for nome, valores in medias.items():
        media = sum(valores) / len(valores)
        medias_finais.append((nome, media))
    
    medias_finais.sort(key=lambda x: x[1])
    
    return medias_finais


def criar_fila_com_medias():
    lista, clientes = inserir_clientes_na_lista()
    medias_finais = calcular_media(lista)

    fila = FilaCircular()

    for nome, media in medias_finais:
        fila.inserir(media)
    
    while len(fila.fila) > 0:
        media = fila.ler()
        print(media)


criar_fila_com_medias()
