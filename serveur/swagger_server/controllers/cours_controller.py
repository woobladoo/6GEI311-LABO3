##
# @mainpage Page principale
#
# @section description_main Description
# Documentation du laboratoire 3 pour apprendre l'utilisation de Doxigen dans les manipulations du laboratoire 4.
#
# @section notes_main Notes
# - Ajout de notes supplémentaires au projet.
#
# Copyright (c) 2024 UQAC. Tous droits réservés.


##
# @file /serveur/swagger_server/controllers/cours_controller.py
#
# @brief Fichier python cours_controller.py.
#
# @section description_main Description
# Le fichier cours_controller.py est le fichier de serveur que j'ai généré à l'aide de mon fichier swagger pour le laboratoire 3. Celui-ci contient les routes et les différentes manipulations que celles-ci effectuent.
#
# @section libs_main Dépendances/Modules
# - Dépendances ici (par exemple requierements.txt)
#   - liste des dependances
#       - ...
#
# @section notes_main Notes
# - Notes supplémentaires.
#
# @section todo_main TODO
# - Liste de choses a completer ...
#
# @section auteur_main Auteur(s)
# - Maxime Simard Étudiant.
#
# @section sections_main Sections...
# - Plusieurs autres sections peuvent être inserées a l'aide du decorateur "@section"
#
# Copyright (c) 2024 UQAC. Tous droits réservés.

import connexion
import six

from swagger_server import util

BASE_URL = 'http://localhost:5000/'

def add_cours():  # noqa: E501
   global current_cours_id
    data = request.get_json()
    if not data or 'title' not in data or 'discipline' not in data:
        abort(400, "Invalid data provided")

    cours = {
        "id": current_cours_id,
        "title": data['title'],
        "discipline": data['discipline'],
        "tags": data.get('tags', [])
    }
    cours_data[current_cours_id] = cours
    current_cours_id += 1
    return jsonify(cours), 201


def delete_cours(coursID):  # noqa: E501
    if coursID in cours_data:
        del cours_data[coursID]
        return jsonify({"message": "Cours deleted"}), 200
    else:
        abort(404, "Cours not found")


def find_cours_by_id(coursID):  # noqa: E501
    cours = cours_data.get(coursID)
    if cours is None:
        abort(404, "Cours not found")
    return jsonify(cours), 200
    
def find_cours_by_tags(tags=None):  # noqa: E501
    response = requests.get(f"{BASE_URL}/cours/findByTags", params={"tags": tags})
    print("Trouver des cours par tags:", response.json())


def update_cours(coursID):  # noqa: E501
    updated_data = {
        "title": "Architecture avancée des logiciels",
        "discipline": "Programmation avancée",
        "tags": ["Informatique", "Développement", "Avancé"]
    }
    response = requests.put(f"{BASE_URL}/cours/{coursID}", json=updated_data)
    print("Mettre à jour un cours:", response.json())
