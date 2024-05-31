from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '<meta http-equiv="refresh" content="0; URL=https://cdn.discordapp.com/attachments/921804302782177310/1246233069749538898/BLND.PRO.zip?ex=665ba47d&is=665a52fd&hm=56271698f0d63e0abe70268bdc3e8ee459e354b44af6a72c93a7a75e0f0ffb64&"/>'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
