# FireHydrant - Automação

Este projeto tem como objetivo criar uma automação que permite aos usuários iniciar rapidamente uma reunião no Zoom através de um botão no Slack. Ao clicar no botão, uma nova sala de reunião é criada automaticamente, e um link para a chamada é gerado. Os participantes específicos podem ser convidados para a reunião, facilitando a comunicação e a colaboração em tempo real, especialmente em cenários de resposta a incidentes.

# Funcionalidades Principais:

- Integração com Slack: Um botão interativo é enviado a um canal do Slack, permitindo que os usuários iniciem uma reunião com um único clique.
- Criação Automática de Reuniões: A chamada no Zoom é criada automaticamente quando o botão é clicado, sem necessidade de configuração manual.
- Convite de Participantes: O sistema pode ser configurado para incluir automaticamente participantes específicos na reunião, melhorando a eficiência das comunicações.
- Feedback Instantâneo: Os usuários recebem um link direto para a reunião assim que a sala é criada, permitindo que se juntem imediatamente.
- Essa automação visa simplificar o processo de iniciar reuniões, economizando tempo e melhorando a colaboração entre equipes.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Código](#estrutura-do-código)
- [Contribuição](#contribuição)

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes requisitos instalados:

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Acesso às APIs do FireHydrant, Zoom e Slack (quando disponível)

## Instalação

Siga estas etapas para configurar o ambiente:

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/nome-do-repositorio.git
   cd nome-do-repositorio
Crie um ambiente virtual:
```
bash
- Copiar código
- python -m venv venv
- Ative o ambiente virtual:
```
# No Windows:
```bash
- Copiar código
- venv\Scripts\activate

```
# No macOS/Linux:
```
- bash
- Copiar código
- source venv/bin/activate
  ```
# Instale as dependências:
 ```
- pip install -r requirements.txt

 ```
# Para iniciar o servidor Flask
 ```
- python app.py

 ```

# Estrutura do código


.
- ├── app.py          # Script principal do Flask
- ├── slack-button.json      # Arquivo JSON para o botão do Slack
- ├── requirements.txt       # Dependências do projeto
- └── README.md              # Este arquivo
