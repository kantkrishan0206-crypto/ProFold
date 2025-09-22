# -*- coding: UTF-8 -*-
################################################################################
# 
# Project: KrishanCSE Toolkit
# File: main.py
#
# Description:
#   Command-line entry logic for the toolkit.
#
# Author: Krishan Kant (kantkrishan0206@gmail.com)
# Created: 2025-09-22
#
################################################################################

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

__all__ = ["main"]


def main(args=None):
    """Main entry point for the toolkit"""
    from . import demo

    if args is None:
        # If no command-line args provided, read from sys and drop the entry filename
        import sys
        args = sys.argv[1:]

    hello = demo.Hello()
    return hello.run(*args)
