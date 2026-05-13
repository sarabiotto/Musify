class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Fila:
    def __init__(self, nome):
        self.nome = nome
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)
        if self.fim is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            print(f"Fila '{self.nome}' está vazia.")
            return None
        musica = self.inicio.musica
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return musica

    def exibir(self):
        if self.inicio is None:
            print(f"Fila '{self.nome}' está vazia.")
            return
        atual = self.inicio
        while atual is not None:
            print(atual.musica)
            atual = atual.proximo