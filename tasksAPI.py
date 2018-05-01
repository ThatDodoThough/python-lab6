from flask import Flask, jsonify, request
import db

app = Flask(__name__)


"""
Le resources sono solo i tasks.
Get, Create, List, Update, Delete.
Singola risorsa = task -> /tasks/<id> -> GET, DELETE, PUT, POST
Collezione = lista di task -> /tasks -> GET
"""


@app.route("/tasks")
def ListTasks():
    lista = db.showTasks()
    IDs = db.parallelIDs()
    mappa = {}
    index = 0
    for id in IDs:
        #key = str(id)
        #print(key)
        mappa[str(id)] = lista[index]
        index = index + 1
    return jsonify(mappa)

@app.route("/tasks/<name>")
def GetTask(name):
    IDs = db.parallelIDs()
    index = 0
    N = len(IDs)
    while index<N:
        checked = str(IDs[index])
        if checked == name:
            lista = db.showTasks()
            cercato = {checked:lista[index]}
            return jsonify(cercato)
        index = index + 1
    print("Non trovato: " + name)
    return

@app.route("/tasks", methods=["POST"])
def CreateTask():
    newTask = request.json
    #NB: newTask è una mappa con un solo elemento, chiave "testo" e value
    #pari al testo da inserire
    ris=db.newTask(newTask["testo"])
    if (ris==-1):
        print("Errore in db.newTask()")
    return jsonify(newTask)

@app.route("/tasks/<name>", methods=["PUT"])
def UpdateTask(name):
    received = request.json
    #contiene la mappa con
    #"todo":valore

    aggiornato = {"id":name, "todo":received["todo"]}
    ris = db.UpdateTaskByMap(aggiornato)
    if ris==-1:
        print("Errore in db.UpdateTaskByMap()")
    return jsonify(aggiornato)

@app.route("/tasks/<name>", methods=["DELETE"])
def DeleteTask(name):
    db.removeTaskByID(name)
    return jsonify(name)

@app.route("/")
def foo():
    return "Hello World!"

def test():
    with app.app_context():
        mappa = ListTasks().json()
        print(mappa)
    return

if __name__ == "__main__":
    db.init()

    #lista = db.showTasks()
    #print(lista)

    #map = ListTasks()
    #test()
    #print(map)
    app.run()