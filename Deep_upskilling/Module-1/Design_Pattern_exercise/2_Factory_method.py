class DocxHandler:
    def open_file(self):
        print("Handling Word Document...")


class PdfHandler:
    def open_file(self):
        print("Handling PDF Document...")


class XlsxHandler:
    def open_file(self):
        print("Handling Excel Document...")


class DocGenerator:
    def produce_handler(self, format_type):
        if format_type == "docx":
            return DocxHandler()
        elif format_type == "pdf":
            return PdfHandler()
        elif format_type == "xlsx":
            return XlsxHandler()
        else:
            print(f"Error: Unknown format '{format_type}'")
            return None


if __name__ == "__main__":
    generator = DocGenerator()
    
    # Test Word Document Handler
    word_handler = generator.produce_handler("docx")
    if word_handler:
        word_handler.open_file()