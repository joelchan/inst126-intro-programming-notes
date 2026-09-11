"""Colour function calls the way VS Code does.

Pygments tags a bare name identically whether it is a variable or a function
being called, so ``compute_pay(38)`` came out in the variable colour while the
``def compute_pay(...)`` line just above it came out in the function colour.
The palette in ``_static/custom.css`` is a clone of VS Code's, so that mismatch
was visible to students comparing the notes against their editor.

Pylance (what students actually have in VS Code) only emits a semantic token
for a name it can *resolve*.  A call it can't resolve falls back to the
TextMate scope ``meta.function-call.generic.python``, which the default themes
leave uncoloured.  So this promotes exactly two cases to ``Name.Function``:

* a bare name followed by ``(`` when a ``def`` for that name appears in the
  same block
* an attribute followed by ``(``, i.e. a method call

An unknown name such as a misspelled ``pirnt`` is deliberately left alone, both
because that is what VS Code does and because the syntax highlighting chapter
teaches the missing colour as a way to spot the typo.

Registered for ``python`` (static fences) and ``ipython3`` (code cells).
"""

from pygments.lexers import get_lexer_by_name
from pygments.token import Name, Operator, Punctuation

LEXER_NAMES = ("python", "ipython3")


def _next_index(tokens, start):
    """Index of the next token on this line that isn't blank."""
    for position in range(start, len(tokens)):
        value = tokens[position][2]
        if value.strip():
            return position
        if "\n" in value:
            return None
    return None


def _previous_index(tokens, start):
    """Index of the previous token on this line that isn't blank."""
    for position in range(start, -1, -1):
        value = tokens[position][2]
        if value.strip():
            return position
        if "\n" in value:
            return None
    return None


def _is_call(tokens, position):
    following = _next_index(tokens, position + 1)
    if following is None:
        return False
    _, token, value = tokens[following]
    return token is Punctuation and value == "("


def _is_attribute(tokens, position):
    preceding = _previous_index(tokens, position - 1)
    if preceding is None:
        return False
    _, token, value = tokens[preceding]
    return token is Operator and value == "."


class VSCodeCallColours:
    def get_tokens_unprocessed(self, text, *args, **kwargs):
        tokens = list(super().get_tokens_unprocessed(text, *args, **kwargs))
        defined = {value for _, token, value in tokens if token is Name.Function}

        for position, (index, token, value) in enumerate(tokens):
            if token is Name and _is_call(tokens, position):
                if value in defined or _is_attribute(tokens, position):
                    token = Name.Function
            yield index, token, value


def _vscode_lexer(name):
    base = type(get_lexer_by_name(name))
    return type("VSCode" + base.__name__, (VSCodeCallColours, base), {})


def setup(app):
    for name in LEXER_NAMES:
        try:
            app.add_lexer(name, _vscode_lexer(name))
        except Exception:  # a lexer we don't ship shouldn't break the build
            pass
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
