#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except Exception as n:
        printf("Exception: {n}", file=sys.stderr)
    else:
        return result
