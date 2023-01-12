class FileReader:
    def __init__(self, filepath: str):
        self.filepath = filepath
    def read(self) -> str:
        try:
            with open(self.filepath, 'r') as f:
                contained = f.read()
                return contained
        except FileNotFoundError:
            return ""


