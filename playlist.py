class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):
        return (f"[{self.id}] {self.titulo} - {self.artista} "
                f"| Gênero: {self.genero} | BPM: {self.bpm}")
    
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

bib = Biblioteca()
bib.inserir("Faroeste Caboclo", "Legião Urbana", "Rock", 128)
bib.inserir("Cachimbo da Paz", "Gabriel o Pensador", "Hip Hop", 92)
bib.inserir("Game of Thrones", "Ramin Djawadi", "Trilha Sonora", 172)
bib.listar()

