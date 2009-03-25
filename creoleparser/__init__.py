# __init__.py
#
# Copyright (c) 2009 Stephen Day
#
# This module is part of Creoleparser and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php
#
from string import lower
from core import Parser, ArgParser
from dialects import (creole11_base, creole10_base, creepy_base,
                    create_dialect, Creole10)

__docformat__ = 'restructuredtext en'

__version__ = '0.6'

creole2html = Parser(dialect=create_dialect(creole10_base), method='html')
"""This is a pure Creole 1.0 parser created for convenience"""

text2html = Parser(dialect=create_dialect(creole11_base), method='html')
"""This is a Creole 1.0 parser (+ additions) created for convenience"""

parse_args = ArgParser(dialect=creepy_base(name_func=lower), force_strings=True)
"""Function for parsing macro arg_strings using a relaxed xml style"""

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
