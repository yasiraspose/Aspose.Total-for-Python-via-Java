"""
PowerPoint Converter from Yasir using Aspose.Slides for Python via Java.
"""
import aspose.slides as slides

class PPTConverter:
    def convert(self, file_path):
        print(f"Converting PPT: {file_path}")
        pres = slides.Presentation(file_path)
        pres.save("output/yasir-powerpoint/output.html", slides.export.SaveFormat.HTML5)
        pres.save("output/yasir-powerpoint/output.md", slides.export.SaveFormat.MD)
        # pres.save("output/yasir-powerpoint/output.json", slides.export.SaveFormat.JSON)
        print("PPT conversion completed.")
