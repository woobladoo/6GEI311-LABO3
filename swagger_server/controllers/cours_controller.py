import connexion
import six

from swagger_server import util


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
    """Delete cours

    This can only be done by the logged in user. # noqa: E501

    :param coursID: The coursID that needs to be deleted
    :type coursID: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        coursID = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_cours_by_id(coursID):  # noqa: E501
    """Finds cours by ID

    Finds a cours by its ID # noqa: E501

    :param coursID: ID de cours
    :type coursID: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        coursID = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_cours_by_tags(tags=None):  # noqa: E501
    """Finds cours by tags

    Multiple tags can be provided with comma-separated strings. # noqa: E501

    :param tags: Tags to filter by
    :type tags: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tags = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_cours(coursID):  # noqa: E501
    """Modification d&#39;un cours existant

    Modification d&#39;un cours existant # noqa: E501

    :param coursID: ID de cours
    :type coursID: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        coursID = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
