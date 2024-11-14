# Projetos de Visão Computacional

Este repositório contém uma coleção de projetos simples desenvolvidos para explorar conceitos e técnicas de Visão Computacional. Cada pasta contém a implementação referente a um projeto específico.

## Tecnologias Usadas

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![CVZone](https://img.shields.io/badge/cvzone-27338e?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

</div>

## Projetos

- **[Projeto 1 - Reconhecimento de Objetos](./reconhecimento-de-objetos)**
  - Implementação de reconhecimento de objetos com Yolo.

- **[Projeto 2 - Jogo do Dinossauro](./dino)**
  - Aplicação de filtros de detecção de bordas, como pynput e OpenCV.

- **[Projeto 3 - Detector de Faces](./detector-faces)**
  - Aplicação de filtros de detecção de faces, com Haar Cascade.

<!-- - **[Projeto 3 - Rastreamento de Movimento](./rastreamento-de-movimento)**
  - Rastreamento de objetos em movimento usando background subtraction.

- **[Projeto 4 - Classificação de Imagens](./classificacao-de-imagens)**
  - Utilização de um modelo pré-treinado para classificar imagens em categorias. -->

Cada projeto inclui um README próprio com informações detalhadas sobre sua implementação, dependências e como rodar os exemplos.

## Como Executar
### Pré-requisitos

- **Python**
- **OpenCV**
- **CVZone**
- **Numpy**

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

2. Instale as depêndencias:
   ```bash
    python -m pip install -r requirements.txt

    python -m pip install -r requirements-optional.txt # dependências opcionais
   ```

3. Execute o projeto:
   ```bash
   python main.py
   ```