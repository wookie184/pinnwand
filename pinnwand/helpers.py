#!/usr/bin/env python
from typing import Dict

from pygments.lexers import get_all_lexers


def _get_pygments_lexers(add_empty: bool = True) -> Dict[str, str]:
    r = {}
    if add_empty:
        r[""] = ""
    for lexer in get_all_lexers():
        r[lexer[1][0]] = lexer[0]
    return r


def list_languages() -> Dict[str, str]:
    return _get_pygments_lexers(False)
