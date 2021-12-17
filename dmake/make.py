#!/usr/bin/env python
"""
Make
----

A simple script to ease development on a docker container.
"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------


# ---- System
import argparse
import sys
from pathlib import Path

# ---- External
import docker

# ----------------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------------


def get_args() -> dict:
    """Get command line arguments."""
    parser = argparse.ArgumentParser(
        description="Simplify Docker build and clean."
    )
    parser.add_argument("--build", "-b", action="store_true", default=False)
    parser.add_argument("--clean", "-c", action="store_true", default=False)

    the_args = parser.parse_args()

    if not(the_args.build or the_args.clean):
        print("Please provide at least one argument.")
        sys.exit(1)
    if the_args.build and the_args.clean:
        print("Only one options is allowed, please choose only one.")
        sys.exit(1)

    return {
        "build": the_args.build, 
        "clean": the_args.clean
    }

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main():
    """Run the script as a stand alone application."""
    the_args = get_args()
    client = docker.from_env()


    if the_args["build"]:
        print(client.images.list())

    if the_args["clean"]:
        print("Cleaning")

# ----------------------------------------------------------------------------
# Name
# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()

