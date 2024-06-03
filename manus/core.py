# This is a manuscript preparation script for journals
# This script will be used to prepare manuscripts for journals

# Importing the required libraries
from openai import OpenAI
import docx
import pypandoc
from pathlib import Path


class Manuscript:
    def __init__(self, source_file, csl, bib):
        self.sections = []
        self.source_file = source_file
        self.csl = csl
        self.bib = bib

    def read_docx(self, filename):
        # Read a manuscript from a file
        doc = docx.Document(filename)
        for para in doc.paragraphs:
            self.sections.append(para.text)

    def create_pdf(self, output_file):
        # Create a PDF from a manuscript
        pdoc_args = [
            "--citeproc",
            "--csl",
            "./styles/apa.csl",
        ]
        print("PATH:\n\n", Path(self.source_file))
        pypandoc.convert_file(
            Path(self.source_file),
            to="pdf",
            format="md",
            outputfile=output_file,
            extra_args=pdoc_args,
        )


class Citation(Manuscript):
    """A class to represent a citation in any given format

    Attributes:
    Citation: str: The citation in plaintext format
    Format: str: The format of the citation

    Methods:
    to_biblatex: Convert a plaintext citation to a BibLaTeX citation
    to_markdown: Convert a plaintext citation to a markdown citation

    """

    # A class to represent a citation in any given format
    def __init__(self, citation: str, format: str = "plaintext"):
        self.citation = citation

    def to_biblatex(self, client=OpenAI()):
        # Transform plaintext citations to BibLaTeX citations

        # Set the temperature
        temperature = 0.0
        # Set the max tokens
        max_tokens = 1000
        # Set the top p
        top_p = 1
        # Set the frequency penalty
        frequency_penalty = 0.5
        # Set the presence penalty
        presence_penalty = 0.0
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI that converts plaintext citations to biblatex. Only respond with code in plain text. Put citation all on one line. Capitalize the first letter of the citation key. Make the citation key the last name of the first author and, the last two digits of the year of publication. Do not use linebreaks. Use all information, including author, title, and year.",
                },
                {
                    "role": "user",
                    "content": self.citation,
                },
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )
        return Citation(str(completion.choices[0].message.content), "biblatex")

    def to_markdown(self):
        # Transform plaintext citations to markdown citations
        filters = ["pandoc-citeproc"]
        pdoc_args = [
            "-s",
            "-f",
        ]
        output = pypandoc.convert_text(
            self.citation,
            to="markdown",
            format="biblatex",
            extra_args=pdoc_args,
            filters=filters,
        )
        return output
