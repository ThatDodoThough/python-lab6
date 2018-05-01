import requests

base_url = "http://127.0.0.1:5000"

if __name__ == "__main__":
    #mappa = requests.get(base_url + "/tasks").json()
    #print(mappa)

    #elem = requests.get(base_url + "/tasks/" + "3").json()
    #print(elem)

    #aggiungi = {"testo":"Test2 delle RESTful APIs"}
    #requests.post(base_url + "/tasks", json=aggiungi)

    #id_aggiornato = 21
    #aggiorna = {"todo":"aggiornato5"}
    #requests.put(base_url + "/tasks/" + str(id_aggiornato), json = aggiorna)

    id_cancellato = 12
    requests.delete(base_url + "/tasks/" + str(id_cancellato))