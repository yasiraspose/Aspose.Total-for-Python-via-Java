
"""
Barcode Generator from Yasir using Aspose.Barcode for Python via Java.
"""

# barcode_converter.py
import asposebarcode as bar

class BarcodeGeneratorConverter:
    def generate_barcode_image_example(self):
        # Create QR code generator
        generator = bar.Generation.BarcodeGenerator(
            bar.Generation.EncodeTypes.QR, "Hello Aspose!"
        )

        # Set parameters (Python style, not Java getters)
        generator.getParameters().getBarcode().getCodeTextParameters().setLocation(bar.Generation.CodeLocation.BELOW)
        generator.getParameters().getBarcode().getXDimension().setMillimeters(2)

        # Save barcode image
        generator.save("output/yasir-barcode/output.png", bar.Generation.BarCodeImageFormat.PNG)
        print("QR Code saved as png.")
