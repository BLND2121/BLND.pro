from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '<meta http-equiv="refresh" content="0; URL=https://cdn.discordapp.com/attachments/976544075530534912/1246227211955212350/00dccbda95586cbd6c6c5fe9f90a45f0.jpg?ex=665b9f09&is=665a4d89&hm=52b9cd06af1a5d5834e998bbf65f0dada98143cea3a5c9370391564febe5ceda&"/>'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
