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
m = Musica(1, "Faroeste Caboclo", "Legião Urbana", "Rock", 128)
print(m)