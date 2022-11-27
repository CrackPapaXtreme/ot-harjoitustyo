import unittest
import json
from usermgmt import UserMgr
from get_local_dir import src

umgr = UserMgr()


class TestCreateUser(unittest.TestCase):
    def test_reset_users_json(self):
        umgr.reset_users_json()
        with open(src("users.json"), "r") as file:
            content = json.load(file)
        self.assertEqual([{"name": "admin", "id": 0, "displayname": "admin",
                         "highscores": {}, "submissions": []}], content)

    def test_create_user(self):
        umgr.reset_users_json()
        # creates two users and checks if they are written
        self.assertTrue(umgr.create_user("nati"))
        self.assertTrue(umgr.create_user("CrackPapaXtreme"))
        with open(src("users.json"), "r") as file:
            content = json.load(file)
        self.assertEqual(
            [
                {
                    "name": "admin",
                    "id": 0,
                    "displayname": "admin",
                    "highscores": {},
                    "submissions": []
                },
                {
                    "name": "nati",
                    "id": 1,
                    "displayname": "nati",
                    "highscores": {},
                    "submissions": []
                },
                {
                    "name": "crackpapaxtreme",
                    "id": 2,
                    "displayname": "CrackPapaXtreme",
                    "highscores": {},
                    "submissions": []
                }
            ], content)

    def test_username_too_long(self):
        umgr.reset_users_json()
        self.assertFalse(umgr.create_user(
            "this_username_is_longer_than_24_characters"))

    def test_username_taken(self):
        umgr.reset_users_json()
        umgr.create_user("username_taken")
        self.assertFalse(umgr.create_user("username_taken"))

    def test_get_user_id_from_name(self):
        umgr.reset_users_json()
        umgr.create_user("name")
        umgr.create_user("eman")
        self.assertEqual(umgr.get_user_id("name"), 1)
        self.assertEqual(umgr.get_user_id("eman"), 2)

    def test_get_user_id_from_nonexistent_user_returns_none(self):
        umgr.reset_users_json()
        self.assertIsNone(umgr.get_user_id("this user doesn't exist"))
