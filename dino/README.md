## Descrição

Uma implementação do jogo do Dinossauro onde os controles e movimentos dentro do jogo são capturados por movimentos detectados pela camera do usuário. Criado utilizando OpenCV e o Pynput.

## Como Executar
### Pré-requisitos

- **Python**
- **OpenCV**
- **Pynput**

### Passos para execução

1. Crie um ambiente virtual venv:
   ```bash
    python -m venv venv # Crie o ambiente

   source venv/bin/activate  # No macOS/Linux
    .\venv\Scripts\activate    # No Windows
   ```

2. Instale as depêndencias:
   ```bash
    python -m pip install -r requirements-dino.txt
   ```

3. Execute o arquivo python:
   ```bash
   python Camera.py
   ```