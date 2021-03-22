from pathlib import Path


class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.source
        directory = directory.relative_to(path)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            self.create_dir(path) if path.is_dir() else None
