from libwyag.repository import Repository

def define_parser(argsubparsers):
    """Defines the argument parser for the 'add' command."""
    parser = argsubparsers.add_parser("add", help="Add file contents to the index")
    parser.add_argument("paths", nargs="+", help="Paths of files to add")

def execute(args):
    """Executes the 'add' command."""
    repo = Repository()
    for path in args.paths:
        print(f"Adding {path} to the index...")
        repo.add_to_index(path)
