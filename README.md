# CommitChat - TikTok Live Chat Display

Um sistema simples para exibir mensagens de chat ao vivo do TikTok em uma interface web limpa e moderna.

## Dependências Necessárias

Antes de executar o projeto, instale as seguintes dependências usando pip:

```bash
pip install flask
pip install TikTokLive
```

Ou cria um arquivo `requirements.txt` com o seguinte conteúdo:

```
flask
TikTokLive
```

E instale com:

```bash
pip install -r requirements.txt
```

## Como Funciona

Este projeto conecta-se a um stream ao vivo do TikTok e exibe as mensagens de chat em tempo real em uma página web.

### Arquivos Importantes

- **`server.py`**: Servidor principal que conecta ao TikTok Live e captura mensagens
- **`servertest.py`**: Versão de teste com mensagens falsas (sem necessidade de conexão TikTok)
- **`templates/index.html`**: Template HTML para exibir o chat

## Como Usar

### 1. Para Testar (Sem TikTok)

Execute o servidor de teste para ver como fica a interface:

```bash
python servertest.py
```

Acesse `http://localhost:5000` no navegador para ver mensagens de exemplo.

### 2. Para Produção (Com TikTok Live)

1. Abra `server.py`
2. Substitua `"NOME_DA_CONTA"` pela conta TikTok real (ex: `"@commitpt"` ou apenas `"commitpt"`)
3. Execute o servidor:

```bash
python server.py
```

O servidor irá:
- Iniciar o Flask em `http://localhost:5000`
- Conectar automaticamente ao stream TikTok Live
- Capturar mensagens em tempo real

**Nota**: Certifique-se de que a conta TikTok está em live no momento da execução. Para ver novas mensagens, recarregue a página no navegador.

## Como Funciona a Conexão TikTok

- O `TikTokLive` conecta-se ao stream ao vivo usando o `unique_id` (nome da conta)
- Captura eventos de comentários em tempo real
- Armazena as últimas 20 mensagens na lista `mensagens`
- A página web atualiza automaticamente mostrando as mensagens mais recentes

## Estrutura do Projeto

```
commitchat/
├── templates/
│   └── index.html      # Interface do chat
├── server.py           # Servidor TikTok Live
├── servertest.py       # Servidor de teste
└── README.md           # Este arquivo
```

## Personalização

- Edite `templates/index.html` para alterar o design do chat se nao gostares deste 
- Modifique o número de mensagens exibidas em `server.py` (atualmente 20)
- Adapte as cores e estilos conforme necessário
