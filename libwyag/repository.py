import os

class Repository:
    """Represents a Git repository."""

    def __init__(self, path=".", create=False):
        self.path = os.path.abspath(path)
        if create:
            self.init()

    def init(self):
        """Initialize a new repository."""
        if os.path.exists(os.path.join(self.path, ".git")):
            raise Exception("Repository already exists!")
        os.makedirs(os.path.join(self.path, ".git", "objects"))
        os.makedirs(os.path.join(self.path, ".git", "refs"))
        print(f"Initialized empty Git repository in {self.path}/.git")
