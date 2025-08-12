"""
Excel Converter from Yasir using Aspose.Cells for Python via Java.
"""
import aspose.cells as cells

class ExcelConverter:
    def convert(self, file_path):
        print(f"Converting Excel: {file_path}")
        workbook = cells.Workbook(file_path)
        workbook.save("output/yasir-excel/output.html", cells.SaveFormat.HTML)
        workbook.save("output/yasir-excel/output.md", cells.SaveFormat.MARKDOWN)
        workbook.save("output/yasir-excel/output.json", cells.SaveFormat.JSON)
        print("Excel conversion completed.")
