#!/usr/bin/env python

from optparse import OptionParser
from controller import get_pit, create_pit, update_pit, remove_pit, list_pits, pit

def main():
    parser = OptionParser(usage="usage: %prog [action] name", version="%prog v0.1")

    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.print_version()
        print "";
        parser.print_usage()
        return 0

    if args[0] == 'create':
        if not args[2]:
            parser.error("The create action requires an argument")
        if get_pit(args[1]):
            parser.error("A pit with this name already exists")

        return create_pit(args[1], args[2])
    elif args[0] == 'update':
        if not args[2]:
            parser.error("The update action requires an argument")
        if not get_pit(args[1]):
            parser.error("A pit with this name does not exists")

        return update_pit(args[1], args[2])
    elif args[0] == 'remove':
        if not get_pit(args[1]):
            parser.error("A pit with this name does not exists")

        return remove_pit(args[1])
    elif args[0] == 'list':
        return list_pits()
    else:
        if not get_pit(args[0]):
            parser.error("A pit with this name does not exists")

        return pit(args[0])


if __name__ == '__main__':
    main()