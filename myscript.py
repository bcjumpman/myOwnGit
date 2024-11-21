import argparse
import sys
from libwyag.commands import (
    cmd_add,
    cmd_cat_file,
    cmd_check_ignore,
    cmd_checkout,
    cmd_commit,
    cmd_hash_object,
    cmd_init,
    cmd_log,
    cmd_ls_files,
    cmd_ls_tree,
    cmd_rev_parse,
    cmd_rm,
    cmd_show_ref,
    cmd_status,
    cmd_tag,
)

# Initialize the argument parser
argparser = argparse.ArgumentParser(description="The coolest content tracker! Check it out!")

# Add subparsers for commands
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

# Define arguments for each command
cmd_add.define_parser(argsubparsers)
cmd_cat_file.define_parser(argsubparsers)
cmd_check_ignore.define_parser(argsubparsers)
cmd_checkout.define_parser(argsubparsers)
cmd_commit.define_parser(argsubparsers)
cmd_hash_object.define_parser(argsubparsers)
cmd_init.define_parser(argsubparsers)
cmd_log.define_parser(argsubparsers)
cmd_ls_files.define_parser(argsubparsers)
cmd_ls_tree.define_parser(argsubparsers)
cmd_rev_parse.define_parser(argsubparsers)
cmd_rm.define_parser(argsubparsers)
cmd_show_ref.define_parser(argsubparsers)
cmd_status.define_parser(argsubparsers)
cmd_tag.define_parser(argsubparsers)

def main(argv=sys.argv[1:]):
    """Main function to parse arguments and execute commands."""
    args = argparser.parse_args(argv)

    # Dispatch the appropriate command using if-elif-else
    if args.command == "add":
        cmd_add.execute(args)
    elif args.command == "cat-file":
        cmd_cat_file.execute(args)
    elif args.command == "check-ignore":
        cmd_check_ignore.execute(args)
    elif args.command == "checkout":
        cmd_checkout.execute(args)
    elif args.command == "commit":
        cmd_commit.execute(args)
    elif args.command == "hash-object":
        cmd_hash_object.execute(args)
    elif args.command == "init":
        cmd_init.execute(args)
    elif args.command == "log":
        cmd_log.execute(args)
    elif args.command == "ls-files":
        cmd_ls_files.execute(args)
    elif args.command == "ls-tree":
        cmd_ls_tree.execute(args)
    elif args.command == "rev-parse":
        cmd_rev_parse.execute(args)
    elif args.command == "rm":
        cmd_rm.execute(args)
    elif args.command == "show-ref":
        cmd_show_ref.execute(args)
    elif args.command == "status":
        cmd_status.execute(args)
    elif args.command == "tag":
        cmd_tag.execute(args)
    else:
        print("Bad command.")

if __name__ == "__main__":
    main()
