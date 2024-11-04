from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Stockage temporaire en mémoire
cours_data = {}
seances_data = {}
current_cours_id = 1
current_seance_id = 1

# Routes pour les cours
@app.route('/cours', methods=['POST'])
def add_cours():
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

@app.route('/cours/<int:coursID>', methods=['GET'])
def get_cours(coursID):
    cours = cours_data.get(coursID)
    if cours is None:
        abort(404, "Cours not found")
    return jsonify(cours), 200

@app.route('/cours/<int:coursID>', methods=['PUT'])
def update_cours(coursID):
    data = request.get_json()
    cours = cours_data.get(coursID)
    if cours is None:
        abort(404, "Cours not found")

    cours.update({
        "title": data.get('title', cours['title']),
        "discipline": data.get('discipline', cours['discipline']),
        "tags": data.get('tags', cours['tags'])
    })
    return jsonify(cours), 200

@app.route('/cours/<int:coursID>', methods=['DELETE'])
def delete_cours(coursID):
    if coursID in cours_data:
        del cours_data[coursID]
        return jsonify({"message": "Cours deleted"}), 200
    else:
        abort(404, "Cours not found")

@app.route('/cours/findByTags', methods=['GET'])
def find_cours_by_tags():
    tags = request.args.getlist('tags')
    filtered_cours = [c for c in cours_data.values() if set(tags).issubset(set(c.get('tags', [])))]
    return jsonify(filtered_cours), 200

# Routes pour les séances
@app.route('/cours/seance', methods=['POST'])
def create_seance():
    global current_seance_id
    data = request.get_json()
    coursID = request.args.get('coursID')
    if not coursID or not data or 'title' not in data or 'weekNumber' not in data or 'theme' not in data:
        abort(400, "Invalid data or missing coursID")

    seance = {
        "id": current_seance_id,
        "title": data['title'],
        "weekNumber": data['weekNumber'],
        "theme": data['theme'],
        "coursID": int(coursID)
    }
    seances_data[current_seance_id] = seance
    current_seance_id += 1
    return jsonify(seance), 201

@app.route('/cours/seance/<int:seanceID>', methods=['GET'])
def get_seance(seanceID):
    seance = seances_data.get(seanceID)
    if seance is None:
        abort(404, "Seance not found")
    return jsonify(seance), 200

@app.route('/cours/seance/<int:seanceID>', methods=['DELETE'])
def delete_seance(seanceID):
    if seanceID in seances_data:
        del seances_data[seanceID]
        return jsonify({"message": "Seance deleted"}), 200
    else:
        abort(404, "Seance not found")

@app.route('/cours/seance/findByModule', methods=['GET'])
def find_seance_by_module():
    module = request.args.get('Module')
    if not module:
        abort(400, "Module parameter is required")

    filtered_seances = [s for s in seances_data.values() if s.get('theme') == module]
    return jsonify(filtered_seances), 200

@app.route('/cours/seance/findBySemaine', methods=['GET'])
def find_seance_by_semaine():
    semaine = request.args.get('Semaine')
    if not semaine:
        abort(400, "Semaine parameter is required")

    filtered_seances = [s for s in seances_data.values() if s.get('weekNumber') == int(semaine)]
    return jsonify(filtered_seances), 200

# Error handler
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)

