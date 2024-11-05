import requests

BASE_URL = 'http://localhost:5000/'

# Ajouter un cours
def add_cours():
    cours_data = {
        "title": "Architecture des logiciels",
        "discipline": "Programmation",
        "tags": ["Informatique", "Développement"]
    }
    response = requests.post(f'{BASE_URL}/cours', json=cours_data)
    print("Ajouter un cours:", response.json())

# Obtenir un cours par ID
def get_cours(coursID):
    response = requests.get(f"{BASE_URL}/cours/{coursID}")
    print("Obtenir un cours:", response.json())

# Mettre à jour un cours
def update_cours(coursID):
    updated_data = {
        "title": "Architecture avancée des logiciels",
        "discipline": "Programmation avancée",
        "tags": ["Informatique", "Développement", "Avancé"]
    }
    response = requests.put(f"{BASE_URL}/cours/{coursID}", json=updated_data)
    print("Mettre à jour un cours:", response.json())

# Supprimer un cours
def delete_cours(coursID):
    response = requests.delete(f"{BASE_URL}/cours/{coursID}")
    print("Supprimer un cours:", response.json())

# Rechercher des cours par tags
def find_cours_by_tags(tags):
    response = requests.get(f"{BASE_URL}/cours/findByTags", params={"tags": tags})
    print("Trouver des cours par tags:", response.json())

# Créer une séance
def create_seance(coursID):
    seance_data = {
        "coursID": coursID,
        "title": "Introduction aux API",
        "weekNumber": 1,
        "theme": "Chapitre 1"
    }
    response = requests.post(f"{BASE_URL}/cours/seance", json=seance_data)
    print("Créer une séance:", response.json())

# Obtenir une séance par ID
def get_seance(seanceID):
    response = requests.get(f"{BASE_URL}/cours/seance/{seanceID}")
    print("Obtenir une séance:", response.json())

# Supprimer une séance
def delete_seance(seanceID):
    response = requests.delete(f"{BASE_URL}/cours/seance/{seanceID}")
    print("Supprimer une séance:", response.json())

# Rechercher des séances par module
def find_seance_by_module(module):
    response = requests.get(f"{BASE_URL}/cours/seance/findByModule", params={"Module": module})
    print("Trouver des séances par module:", response.json())

# Rechercher des séances par semaine
def find_seance_by_semaine(semaine):
    response = requests.get(f"{BASE_URL}/cours/seance/findBySemaine", params={"Semaine": semaine})
    print("Trouver des séances par semaine:", response.json())

if __name__ == '__main__':
    # Exemples d'appels
    add_cours()                 # Ajouter un cours
    get_cours(1)                # Obtenir le cours avec ID 1
    update_cours(1)             # Mettre à jour le cours avec ID 1
    delete_cours(1)             # Supprimer le cours avec ID 1
    get_cours(1)                # Obtenir le cours avec ID 1
    add_cours()                 # Ajouter un cours
    find_cours_by_tags(["Informatique"])  # Trouver des cours avec un tag spécifique
    create_seance(2)           # Créer une séance pour le cours avec ID 1
    get_seance(1)              # Obtenir la séance avec ID 1
    delete_seance(1)           # Supprimer la séance avec ID 1
    get_seance(1)               # Obtenir la séance avec ID 1
    create_seance(2)           # Créer une séance pour le cours avec ID 1
    find_seance_by_module("Chapitre 1")  # Trouver des séances par module
    find_seance_by_semaine(1)  # Trouver des séances par semaine
