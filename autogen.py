#!/usr/bin/env python
import argparse
import logging
import os
import random
import sys

parser = argparse.ArgumentParser(usage="%(prog)s [options] args...")
parser.add_argument("-v", action="append_const", const=1, dest="verbosity", default=[],
                    help="Be more verbose. Can be specified multiple times to increase verbosity further")
parser.add_argument("--smtp-server", required=True)
parser.add_argument("--root-url", required=True)
parser.add_argument("--server-email", required=True)
parser.add_argument("--target", required=True)

_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

def main(args):
    with open(os.path.join(_ROOT_DIR, "vars.yml"), "w") as outfile:
        with open(os.path.join(_ROOT_DIR, "vars.yml.in")) as infile:
            outfile.write(infile.read().format(secret_key=_gen_secret_key(), **vars(args)))
    with open(os.path.join(_ROOT_DIR, "inventory"), "w") as outfile:
        outfile.write("[target]\n")
        outfile.write(args.target)
    return 0

def _gen_secret_key():
    return "".join(chr(random.randrange(256)) for i in range(50)).encode("base64").strip()

################################## Boilerplate ################################
def _configure_logging(args):
    verbosity_level = len(args.verbosity)
    if verbosity_level == 0:
        level = "WARNING"
    elif verbosity_level == 1:
        level = "INFO"
    else:
        level = "DEBUG"
    logging.basicConfig(
        stream=sys.stderr,
        level=level,
        format="%(asctime)s -- %(message)s"
        )


#### For use with entry_points/console_scripts
def main_entry_point():
    args = parser.parse_args()
    _configure_logging(args)
    sys.exit(main(args))


if __name__ == "__main__":
    main_entry_point()
