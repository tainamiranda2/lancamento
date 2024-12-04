
# 🏀 **Simulador de Lançamento Oblíquo - Basquete**

Este projeto é um jogo simples em **Pygame** que simula o lançamento de uma bola de basquete em um movimento oblíquo. A bola é lançada em direção à cesta com uma trajetória realista, considerando a força da gravidade. O jogador pode visualizar a trajetória da bola representada por um pontilhado preto, ajudando a compreender os lançamentos.

## 🚀 **Como funciona?**

- A bola é lançada a partir de uma posição fixa com uma velocidade inicial (`v0`) e um ângulo (`angle`).
- A trajetória do lançamento é simulada usando as equações do movimento oblíquo.
- A cesta está posicionada no canto superior direito da tela.
- O jogo registra o número de **acertos** e **erros**.
- Um pontilhado preto exibe a trajetória da bola durante o lançamento.

---

## 🎮 **Controles do Jogo**

- O jogo inicia automaticamente com lançamentos aleatórios.
- Os parâmetros de velocidade (`v0`) e ângulo (`angle`) variam dentro de valores pré-definidos, simulando lançamentos diferentes.

---

## 📂 **Estrutura do Projeto**

```plaintext
.
├── quadra.png      # Imagem de fundo (quadra de basquete)
├── cesta.png       # Imagem da cesta
├── bola.png        # Imagem da bola
├── main.py         # Código principal do jogo
└── README.md       # Documentação do projeto
```

---

## 🛠️ **Como executar o jogo**

1. Certifique-se de ter o **Python** instalado na sua máquina (versão 3.8 ou superior).
2. Instale o **Pygame** com o comando:
   ```bash
   pip install pygame
   ```
3. Baixe ou clone este repositório:
   ```bash
   git clone https://github.com/tainamiranda2/lancamento
   cd lancamento
   ```
4. Execute o jogo:
   ```bash
   python main.py
   ```

---

## 📊 **Regras do Jogo**

- A cada lançamento, o programa verifica se a bola atinge a cesta.
- **Acerto**: A bola passa dentro do espaço da cesta.
- **Erro**: A bola não atinge a cesta.

---

## 🖼️ **Elementos Gráficos**

- **Quadra**: Representa o ambiente de jogo.
- **Cesta**: Posicionada no canto superior direito.
- **Bola**: Simula o objeto lançado.
- **Trajetória**: Um pontilhado preto ilustra o caminho percorrido pela bola.

---

## 🔮 **Equações Utilizadas**

O movimento da bola segue as equações do movimento oblíquo:

- **Posição horizontal (`x`)**:
  \[
  x = x_{\text{inicial}} + v_0 \cdot \cos(\theta) \cdot t
  \]

- **Posição vertical (`y`)**:
  \[
  y = y_{\text{inicial}} - \left(v_0 \cdot \sin(\theta) \cdot t - \frac{1}{2} \cdot g \cdot t^2\right)
  \]

---

## 👩‍💻 **Personalização**

- **Velocidade inicial**: Alterar o intervalo `random.uniform(30, 60)` para definir os valores possíveis de lançamento.
- **Ângulo**: Alterar `random.uniform(30, 60)` para ajustar o ângulo de lançamento.
- **Dimensões e posição da cesta**: Modifique `hoop_x` e `hoop_y` para reposicionar a cesta.

---
