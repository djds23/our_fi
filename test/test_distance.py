import unittest

from our_fi.distance import distance


class TestDistance(unittest.TestCase):

    def test_same_distance(self):
        point_one = (100, 100)
        point_two = (100, 100)
        self.assertEqual(distance(point_one, point_two), 0)

    def test_different(self):
        point_one = (100, 100)
        point_two = (50, 50)
        self.assertEqual(int(distance(point_one, point_two)), 70)


