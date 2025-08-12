"""
Main entry point for the Aspose for Python via Java.
This script allows converting PDF, Word, Excel, and PowerPoint to Markdown, JSON, and HTML.
"""

from converters.pdf_converter import PDFConverter
from converters.word_converter import WordConverter
from converters.excel_converter import ExcelConverter
from converters.ppt_converter import PPTConverter

def main():
    print("Aspose Document Processing Solution")
    print("This example converts files to Markdown, JSON, and HTML formats using Aspose for Python via Java.")

    # Example usage (replace with your file paths)
    pdf_path = "sample_files/sample.pdf"
    # word_path = "sample_files/sample.docx"
    excel_path = "sample_files/sample.xlsx"
    # ppt_path = "sample_files/sample.pptx"

    PDFConverter().convert(pdf_path)
    # WordConverter().convert(word_path)
    ExcelConverter().convert(excel_path)
    # PPTConverter().convert(ppt_path)

if __name__ == "__main__":
    main()
