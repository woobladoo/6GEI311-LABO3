import connexion
import six

from swagger_server import util


def create_seance():  # noqa: E501
    """création d&#39;une seance

    création d&#39;une seance # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def delete_seance(seanceID):  # noqa: E501
    """Suppression d&#39;une seance d&#39;un cours

    Suppression d&#39;une séance # noqa: E501

    :param seanceID: ID de la seance
    :type seanceID: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        seanceID = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_seance(seanceID):  # noqa: E501
    """Trouver une seance selon ID spécifique

    Trouver une seance selon ID spécifique # noqa: E501

    :param seanceID: ID de la seance
    :type seanceID: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        seanceID = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def seance_find_by_module(Module):  # noqa: E501
    """Trouver la séance selon un module spécifique

    Trouver la séance selon un module spécifique # noqa: E501

    :param Module: Nom du module
    :type Module: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Module = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def seance_find_by_semaine(Semaine):  # noqa: E501
    """Trouver la séance selon une semaine

    Trouver la séance selon une semaine # noqa: E501

    :param Semaine: Nombre de la semaine
    :type Semaine: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Semaine = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
