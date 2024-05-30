import unittest
from manus.core import Bibliography


class TestBibliography(unittest.TestCase):
    def test_bibliography_get_biblatex(self):
        bibliography = Bibliography(
            [
                "The Art of Computer Programming, Donald Knuth 1968",
                "Attention is all you Need, Vaswani et al. 2017",
            ]
        )
        self.assertEqual(
            bibliography.to_biblatex(citations),
            [
                "@book{Knuth68, author = {Donald Knuth}, title = {The Art of Computer Programming}, year = {1968}}",
                "@article{Vaswani17, author = {Vaswani et al.}, title = {Attention is all you Need}, year = {2017}}",
            ],
            "biblatex",
        )
