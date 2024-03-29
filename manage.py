#!/usr/bin/env python

from os import environ
from sys import argv


def main():
    environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exception:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exception
    execute_from_command_line(argv)


if __name__ == "__main__":
    main()
