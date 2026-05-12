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
    
m1 = Musica(1, "Faroeste Caboclo", "Legião Urbana", "Rock", 128)
m2 = Musica(2, "Se", "Djavan", "MPB", 76)

n1 = NodoLista(m1)
n2 = NodoLista(m2)

n1.proximo = n2  

print(n1.musica)        
print(n1.proximo.musica)

