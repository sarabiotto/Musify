from modelo.musica import Musica
from estrutura.lista_encadeada import Biblioteca
from estrutura.fila import Fila


def main():
    biblioteca = Biblioteca()
    filas = {
        "relaxar": Fila("Relaxar"),
        "focar":   Fila("Focar"),
        "animar":  Fila("Animar"),
        "treinar": Fila("Treinar")
    }
    historico = Fila("Histórico")

    biblioteca.inserir("Evidências", "Chitãozinho & Xororó", "Sertanejo", 112)
    biblioteca.inserir("Faroeste Caboclo", "Legião Urbana", "Rock", 128)
    biblioteca.inserir("Se", "Djavan", "MPB", 76)
    biblioteca.inserir("He-Man", "Trem da Alegria", "Infantil", 136)
    biblioteca.inserir("O Homem Que Não Tinha Nada", "Projota", "Rap", 84)

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

        elif opcao == "5":
            for nome in filas:
                filas[nome].inicio = None
                filas[nome].fim = None
                filas[nome].tamanho = 0
            atual = biblioteca.cabeca
            while atual is not None:
                bpm = atual.musica.bpm
                if bpm <= 80:
                    filas["relaxar"].enqueue(atual.musica)
                elif bpm <= 120:
                    filas["focar"].enqueue(atual.musica)
                elif bpm <= 160:
                    filas["animar"].enqueue(atual.musica)
                else:
                    filas["treinar"].enqueue(atual.musica)
                atual = atual.proximo
            print("Filas montadas com sucesso!")

        elif opcao == "6":
            print("Filas: relaxar, focar, animar, treinar")
            nome = input("Escolha a fila: ").lower()
            if nome not in filas:
                print("Fila inválida.")
            else:
                musica = filas[nome].dequeue()
                if musica:
                    print("Reproduzindo:", musica)
                    historico.enqueue(musica)

        elif opcao == "7":
            print("Filas: relaxar, focar, animar, treinar")
            nome = input("Escolha a fila: ").lower()
            if nome not in filas:
                print("Fila inválida.")
            else:
                filas[nome].exibir()

        elif opcao == "8":
            historico.exibir()

        elif opcao == "9":
            print(f"\nTotal na biblioteca: {biblioteca.tamanho}")
            for nome, fila in filas.items():
                print(f"Fila {fila.nome}: {fila.tamanho} músicas")
            print(f"Total reproduzidas: {historico.tamanho}")

        elif opcao == "10":
            print("Saindo...")
            break


if __name__ == "__main__":
    main()