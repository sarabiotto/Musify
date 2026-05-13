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

def main():
    biblioteca = Biblioteca()
    filas = {
        "relaxar": Fila("Relaxar"),
        "focar":   Fila("Focar"),
        "animar":  Fila("Animar"),
        "treinar": Fila("Treinar")
    }
    historico = Fila("Histórico")

    while True:
        print("\n===== MUSIFY =====")
        print("1. Adicionar música")
        print("2. Remover música")
        print("3. Buscar música")
        print("4. Listar biblioteca")
        print("5. Montar filas por humor")
        print("6. Reproduzir próxima")
        print("7. Exibir fila de humor")
        print("8. Exibir histórico")
        print("9. Estatísticas")
        print("10. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            artista = input("Artista: ")
            genero = input("Gênero: ")
            bpm = input("BPM: ")
            if not bpm.isnumeric() or int(bpm) <= 0:
                print("BPM inválido!")
            else:
                biblioteca.inserir(titulo, artista, genero, int(bpm))

        elif opcao == "2":
            id = int(input("ID da música: "))
            biblioteca.remover(id)

        elif opcao == "3":
            valor = input("Digite o ID ou título: ")
            if valor.isnumeric():
                valor = int(valor)
            musica = biblioteca.buscar(valor)
            if musica:
                print(musica)
            else:
                print("Música não encontrada.")

        elif opcao == "4":
            biblioteca.listar()

        elif opcao == "10":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()



