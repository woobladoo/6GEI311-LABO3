# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestSeanceController(BaseTestCase):
    """SeanceController integration test stubs"""

    def test_create_seance(self):
        """Test case for create_seance

        création d'une seance
        """
        response = self.client.open(
            '/cours/seance',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_seance(self):
        """Test case for delete_seance

        Suppression d'une seance d'un cours
        """
        query_string = [('seanceID', None)]
        response = self.client.open(
            '/cours/seance/{seanceID}',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_seance(self):
        """Test case for find_seance

        Trouver une seance selon ID spécifique
        """
        response = self.client.open(
            '/cours/seance/{seanceID}'.format(seanceID=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_seance_find_by_module(self):
        """Test case for seance_find_by_module

        Trouver la séance selon un module spécifique
        """
        query_string = [('Module', None)]
        response = self.client.open(
            '/cours/seance/findByModule',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_seance_find_by_semaine(self):
        """Test case for seance_find_by_semaine

        Trouver la séance selon une semaine
        """
        query_string = [('Semaine', None)]
        response = self.client.open(
            '/cours/seance/findBySemaine',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
