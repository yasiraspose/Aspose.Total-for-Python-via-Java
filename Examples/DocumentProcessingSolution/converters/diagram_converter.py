
"""
Diagram Converter from Yasir using Aspose.Diagram for Python via Java.
"""

# diagram_converter.py
import asposediagram.api as diagram

class DiagramConverter:
    def convert(self, input_file):

        # Load a Visio diagram from the input file.
        # The DiagramConverter class is the main entry point for working with Visio files.
        print(f"Loading diagram from '{input_file}'...")

        # Access Java classes via Python bridge
        Diagram = diagram.Diagram
        ImageSaveOptions = diagram.ImageSaveOptions
        SaveFileFormat = diagram.SaveFileFormat

        diag = Diagram(input_file)

        print("Diagram loaded successfully.")

        # Configure image save options
        options = ImageSaveOptions(SaveFileFormat.PNG)
        options.setPageIndex(0)  # Save only the first page (index starts at 0)

        # Save the diagram as PNG
        diag.save("output/yasir-diagram/output.png", options)

        print("Visio page saved as PNG successfully.")