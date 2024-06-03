import os
import unittest
from manus.core import Manuscript


class TestManuscript(unittest.TestCase):
    def test_create_manuscript(self):
        manuscript = Manuscript(
            source_file="../tests/files/anthropocene.md",
            csl="apa",
            bib="bibliography.bib",
        )
        self.assertIsInstance(manuscript, Manuscript)

    def test_create_pdf(self):
        manuscript = Manuscript(
            source_file="anthropocene.md",
            csl="apa",
            bib="bibliography.bib",
        )
        manuscript.create_pdf("anthropocene.pdf")

        self.assertTrue(os.path.exists("anthropocene.pdf"))

    def test_read_docx(self):
        manuscript = Manuscript(
            source_file="anthropocene.md",
            csl="apa",
            bib="bibliography.bib",
        )
        manuscript.read_docx("anthropocene.docx")
        self.assertEqual(len(manuscript.sections), 7)


if __name__ == "__main__":
    unittest.main()
