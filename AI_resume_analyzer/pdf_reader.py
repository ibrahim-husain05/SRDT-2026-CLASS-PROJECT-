from PyPDF2 import PdfReader


class PDFReader:
    def extract_text(self, file_path):
        try:
            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            return text

        except Exception as e:
            print("Error reading PDF:", e)
            return None