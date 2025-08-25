"""
PDF Converter from Yasir using Aspose.PDF for Python via Java.
"""

# pdf_converter.py
from asposepdf import Api

class PDFConverter:
    def convert(self, file_path):
        print(f"Converting PDF: {file_path}")

        doc = Api.Document(file_path)
        save_options = Api.HtmlSaveOptions()
        doc.save("output/yasir-pdf/output.html", save_options)
        # doc.save("output/yasir-pdf/output.html", Api.SaveFormat.Html)

        # MarkdownSaveOptions is not in Aspose.PDF, only in Aspose.Words. If you want Markdown, you must combine both libraries (Aspose.PDF + Aspose.Words).
        # Aspose.PDF doesn’t provide a direct Pdf → Json save option. Instead, you do it in two steps: Extract PDF text/content (structured by page, paragraphs, etc.) then serialize that extracted data into JSON using Python’s json module.

        print("PDF conversion completed.")
