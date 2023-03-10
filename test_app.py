from unittest import TestCase

from app import app, games

import json

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- TEST: HOMEPAGE -->', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.get("/api/new-game")
            json_data = response.get_json()
            print(json_data)
            self.assertTrue(json.loads(json_data))
            self.assertEqual(response.status_code, 200)
            # write a test for this route
            # Test route returns JSON w/ string of gameid and list of lists
            # Test that route stores new game in games dictionary
