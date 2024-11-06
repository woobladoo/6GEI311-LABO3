import connexion
import six

from swagger_server import util


def create_seance():  # noqa: E501
    global current_seance_id

    # Get JSON data from the request
    data = request.get_json()

    # Check if data is valid and all required fields are present
    if not data:
        abort(400, "Missing JSON data")
    if 'coursID' not in data or 'title' not in data or 'weekNumber' not in data or 'theme' not in data:
        abort(400, "Invalid data or missing fields (coursID, title, weekNumber, theme)")
    
    # Validate and parse coursID
    try:
        coursID = int(data['coursID'])
    except ValueError:
        abort(400, "coursID must be an integer")

    # Create the seance dictionary with validated data
    seance = {
        "id": current_seance_id,
        "title": data['title'],
        "weekNumber": data['weekNumber'],
        "theme": data['theme'],
        "coursID": coursID
    }

    # Store the new seance and increment the ID
    seances_data[current_seance_id] = seance
    current_seance_id += 1
    return jsonify(seance), 201


def delete_seance(seanceID):  # noqa: E501
    if seanceID in seances_data:
        del seances_data[seanceID]
        return jsonify({"message": "Seance deleted"}), 200
    else:
        abort(404, "Seance not found")


def find_seance(seanceID):  # noqa: E501
    seance = seances_data.get(seanceID)
    if seance is None:
        abort(404, "Seance not found")
    return jsonify(seance), 200


def seance_find_by_module(Module):  # noqa: E501
    module = request.args.get('Module')
    if not module:
        abort(400, "Module parameter is required")

    filtered_seances = [s for s in seances_data.values() if s.get('theme') == module]
    return jsonify(filtered_seances), 200


def seance_find_by_semaine(Semaine):  # noqa: E501
    semaine = request.args.get('Semaine')
    if not semaine:
        abort(400, "Semaine parameter is required")

    filtered_seances = [s for s in seances_data.values() if s.get('weekNumber') == int(semaine)]
    return jsonify(filtered_seances), 200

# def seance_find_by_semaine(Semaine):  # noqa: E501
#     """Trouver la séance selon une semaine

#     Trouver la séance selon une semaine # noqa: E501

#     :param Semaine: Nombre de la semaine
#     :type Semaine: dict | bytes

#     :rtype: None
#     """
#     if connexion.request.is_json:
#         Semaine = .from_dict(connexion.request.get_json())  # noqa: E501
#     return 'do some magic!'