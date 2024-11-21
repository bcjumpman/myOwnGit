def define_parser(subparsers):
    """Defines the parser for the 'add' command."""
    parser = subparsers.add_parser("add", help="Add file contents to the index")
    parser.add_argument("files", nargs="+", help="Files to add")

def execute(args):
    """Executes the 'add' command."""
    print(f"Adding files: {args.files}")
