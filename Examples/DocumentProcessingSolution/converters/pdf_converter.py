"""
PDF Converter from Yasir using Aspose.PDF for Python via Java.
"""
import aspose.pdf as pdf

class PDFConverter:
    def convert(self, file_path):
        print(f"Converting PDF: {file_path}")
        doc = pdf.Document(file_path)
        doc.save("output/yasir-pdf/output.html", pdf.SaveFormat.HTML)
        doc.save("output/yasir-pdf/output.md", pdf.SaveFormat.MARKDOWN)
        # doc.save("output/yasir-pdf/output.json", pdf.SaveFormat.JSON)
        print("PDF conversion completed.")
