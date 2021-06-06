import unittest
from Fixtures.FlatbaseFixture import FlatbaseFixture


class TestURGS(unittest.TestCase):
    def test_u_voyage(self):
        vf = FlatbaseFixture("chrome")
        vf.open_page()
        vf.fill_frame()
        input()