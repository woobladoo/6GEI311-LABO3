# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestCoursController(BaseTestCase):
    """CoursController integration test stubs"""

    def test_add_cours(self):
        """Test case for add_cours

        Add a new cours
        """
        response = self.client.open(
            '/cours',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_cours(self):
        """Test case for delete_cours

        Delete cours
        """
        response = self.client.open(
            '/cours/{coursID}'.format(coursID=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_cours_by_id(self):
        """Test case for find_cours_by_id

        Finds cours by ID
        """
        response = self.client.open(
            '/cours/{coursID}'.format(coursID=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_cours_by_tags(self):
        """Test case for find_cours_by_tags

        Finds cours by tags
        """
        query_string = [('tags', None)]
        response = self.client.open(
            '/cours/findByTags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_cours(self):
        """Test case for update_cours

        Modification d'un cours existant
        """
        response = self.client.open(
            '/cours/{coursID}'.format(coursID=None),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
