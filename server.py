from flask import Flask, render_template
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent
import threading
import time

app = Flask(__name__)
mensagens = []

client = TikTokLiveClient(unique_id="NOME_DA_CONTA")

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    mensagens.append(f"{event.user.nickname}: {event.comment}")

@app.route("/")
def home():
    return render_template("index.html", mensagens=mensagens[-20:])  # últimas 20 mensagens podes colocar mais , nao sei se tem limite

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    # Inicia o servidor Flask em uma thread separada
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Pequena pausa para o Flask iniciar
    time.sleep(2)

    print("Servidor Flask iniciado em http://localhost:5000")
    print("Conectando ao TikTok Live...")

    # Executa o cliente TikTok so na thread principal, e so para quando parar live ou fechar o programa
    client.run()
