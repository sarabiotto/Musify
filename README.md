# Musify

Sistema de playlist desenvolvido como projeto da disciplina de Estrutura de Dados - Fatec Rio Claro.
Professor: Orlando Saraiva Jr.

## Descrição

O sistema permite gerenciar uma biblioteca pessoal de músicas, montar filas de reprodução por humor e consultar o histórico de reproduções.

## Estruturas de Dados utilizadas

- **Lista Encadeada** — armazena a biblioteca de músicas
- **Fila FIFO** — usada para as filas de humor e histórico

## Como executar

Requer Python 3.6 ou superior. Sem dependências externas.

```bash
python main.py
```

## Estrutura do projeto
Musify/
├── modelo/
│   └── musica.py
├── estrutura/
│   ├── fila.py
│   └── lista_encadeada.py
└── main.py


## Filas de humor

| Fila    | Humor        | BPM        |
|---------|--------------|------------|
| Relaxar | Tranquilo    | até 80     |
| Focar   | Concentração | 81 a 120   |
| Animar  | Agitado      | 121 a 160  |
| Treinar | Intenso      | acima de 160 |