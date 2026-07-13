import re


class Preprocessor:

    def clean_text(self, text):
        if not text:
            return ""

        text = text.lower()

        text = re.sub(r"\n", " ", text)
        text = re.sub(r"\t", " ", text)
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[^a-z0-9@.+# ]", " ", text)

        return text.strip()