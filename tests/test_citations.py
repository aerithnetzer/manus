import unittest
from manus.core import Citation
import bibtexparser


class TestCitations(unittest.TestCase):
    def test_citation_get_bibtex(self):
        citation = Citation("The Art of Computer Programming, Donald Knuth 1968")
        bibtex_str = citation.to_biblatex().citation

        try:
            bibtexparser.loads(bibtex_str)
        except bibtexparser.bparser.BibTexParserError as e:
            self.fail(f"BibTeX parsing failed with error: {e}")


if __name__ == "__main__":
    unittest.main()
