# Projetos de Visão Computacional

Este repositório contém uma coleção de projetos simples desenvolvidos para explorar conceitos e técnicas de Visão Computacional. Cada pasta contém a implementação referente a um projeto específico.

## Tecnologias Usadas

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![CVZone](https://img.shields.io/badge/cvzone-27338e?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-013243?style=for-the-badge&logo=python&logoColor=white)


</div>

## Projetos

- **[Projeto 1 - Reconhecimento de Objetos](./reconhecimento-de-objetos/README.md)**
  - Implementação de reconhecedor de objetos com Yolo.

- **[Projeto 2 - Jogo do Dinossauro](./dino/README.md)**
  - Jogo do Dinossauro feito com uso do Pynput e OpenCV.

- **[Projeto 3 - Detector de Faces](./detector-faces/README.md)**
  - Aplicação de filtros de detecção de faces, com Haar Cascade.

- **[Projeto 4 - Detector de Emocoes](./detector-emocoes/README.md)**
  - Aplicação de filtros de detecção de emoções, com Haar Cascade.

Cada projeto inclui um README próprio com informações detalhadas sobre sua implementação, dependências e como rodar os exemplos.

## Como Executar
### Passos para execução

1. Clone o repositório:
   ```fish
   git clone https://github.com/Thigas014/VisaoComputacional.git
   cd VisaoComputacional/
   ```

2. Crie um ambiente virtual venv:
   ```bash
    python -m venv venv # Crie o ambiente

   source venv/bin/activate  # No macOS/Linux
    .\venv\Scripts\activate    # No Windows
   ```

3. Vá para o diretorio do projeto escolhido
   ```bash
   cd dino/ # Diretorio do jogo do Dinossauro

   cd reconhecimento-de-objetos/ # Diretorio do reconhecedor de objetos

   cd detector-faces/ # Diretorio do reconhecedor de faces

   cd detector-emocoes/ # Diretorio do detector de emocoes
   ```

4. Após ter ido para o diretório do projeto de desejado, instale as depêndencias necessárias:
   ```bash
    python -m pip install -r requirements-objetos.txt # depêndencias para o reconhecedor de objetos

    python -m pip install -r requirements-dino.txt # depêndencias para o jogo do dinossauro

    python -m pip install -r requirements-faces.txt # depêndencias para o detector de faces

    python -m pip install -r requirements-emocoes.txt # depêndencias para o reconhecedor de emoções


    python -m pip install -r requirements.txt # Alternativamente, caso queira instalar todas as depedências de todos os projetos
   ```

5. Execute o arquivo py do respectivo projeto:
   ```bash
   python Camera.py # Jogo do Dinossauro

   python Main.py # Reconhecedor de objetos

   python Main.py # Reconhecedor de faces

   python app.py # Detector de emocoes faciais
   ```
