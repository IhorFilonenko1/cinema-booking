import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import movies


class TestMovies(unittest.TestCase):
    def test_list_movies_not_empty(self):
        self.assertGreater(len(movies.list_movies()), 0)

    def test_get_movie_by_id(self):
        movie = movies.get_movie(1)
        self.assertIsNotNone(movie)
        self.assertEqual(movie["id"], 1)

    def test_get_movie_missing(self):
        self.assertIsNone(movies.get_movie(9999))

    def test_add_movie(self):
        before = len(movies.list_movies())
        movie = movies.add_movie("Test", "Test", 2025, 90, 10, 50.0)
        self.assertEqual(len(movies.list_movies()), before + 1)
        self.assertEqual(movie, movies.get_movie(movie["id"]))


if __name__ == "__main__":
    unittest.main()
