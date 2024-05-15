# This is a manuscript preparation script for journals
# This script will be used to prepare manuscripts for journals

# Importing the required libraries
from openai import OpenAI
import docx
import pypandoc


class Citation:
    # A class to represent a plaintext citation
    def __init__(self, citation: str, format: str = "plaintext"):
        self.citation = citation

    if format == "plaintext":

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
            return Citation(str(completion.choices[0].message.content), "plaintext")
    else:
        raise ValueError(f"Unsupported format: {format}")

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


class Bibliography:
    def __init__(self, citations: list):
        self.citations = citations

    def to_markdown(self, citations):
        # Transform a list of citations to a markdown bibliography via pandoc
        pass

    def to_biblatex(self, citations):
        # Transform a list of plaintext citations to a BibLaTeX bibliography
        pass


class Manuscript:
    def __init__(self):
        self.sections = []

    def read_docx(self, filename):
        # Read a manuscript from a file
        doc = docx.Document(filename)
        for para in doc.paragraphs:
            self.sections.append(para.text)
