import unittest
import bufrpy
from .util import read_file

class TestReadBufr(unittest.TestCase):
    def test_sequence(self):
        msg = read_file("data/bt/B0000000000098013001.TXT", "data/bt/D0000000000098013001.TXT", "data/tempLow_200707271955.bufr")

    def test_replication_sequence(self):
        msg = read_file("data/bt/B0000000000098013001.TXT", "data/bt/D0000000000098013001.TXT", "data/1xBUFRSYNOP-ed4.bufr")

    def test_multiple_segments(self):
        msg = read_file("data/bt/B0000000000098013001.TXT", "data/bt/D0000000000098013001.TXT", "data/3xBUFRSYNOP-com.bufr")

    def test_uncompressed_operators(self):
        msg = read_file("data/bt/B0000000000098013001.TXT", "data/bt/D0000000000098013001.TXT", "data/207003.bufr")

    def test_compressed_operators(self):
        msg1 = read_file("data/bt/B0000000000098013001.TXT", "data/bt/D0000000000098013001.TXT", "data/207003.bufr")
        msg2 = read_file("data/bt/B0000000000098013001.TXT", "data/bt/D0000000000098013001.TXT", "data/207003_compressed.bufr")

        assert msg1.section1 == msg2.section1
        assert msg1.section2 == msg2.section2
        assert msg1.section3.descriptors == msg2.section3.descriptors
        assert msg1.section4.subsets == msg2.section4.subsets
        assert msg1.section5 == msg2.section5
