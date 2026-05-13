from models.musica import Musica


class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Biblioteca:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
        self._proximo_id = 1

    def inserir(self, titulo, artista, genero, bpm):
        musica = Musica(self._proximo_id, titulo, artista, genero, bpm)
        self._proximo_id += 1
        novo_nodo = NodoLista(musica)

        if self.cabeca is None:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

        self.tamanho += 1
        print(f"Música '{titulo}' adicionada com ID {musica.id}.")

    def listar(self):
        if self.cabeca is None:
            print("Biblioteca vazia.")
            return
        atual = self.cabeca
        while atual is not None:
            print(atual.musica)
            atual = atual.proximo

    def buscar(self, valor):
        atual = self.cabeca
        while atual is not None:
            if atual.musica.id == valor or atual.musica.titulo == valor:
                return atual.musica
            atual = atual.proximo
        return None

    def remover(self, id):
        anterior = None
        atual = self.cabeca

        while atual is not None:
            if atual.musica.id == id:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                print(f"Música ID {id} removida.")
                return
            anterior = atual
            atual = atual.proximo

        print(f"ID {id} não encontrado.")