import unittest
from manus.core import Citation


class TestCitations(unittest.TestCase):
    def test_citation_get_bibtex(self):
        citation = Citation("The Art of Computer Programming, Donald Knuth 1968")
        self.assertEqual(
            citation.to_biblatex(),
            "@book{Knuth68, author = {Donald Knuth}, title = {The Art of Computer Programming}, year = {1968}}",
        )


if __name__ == "__main__":
    unittest.main()
