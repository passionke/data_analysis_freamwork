from pygments import formatters, highlight, lexers
from pygments_pprint_sql import SqlFilter


def format(raw_sql):
    lexer = lexers.MySqlLexer()
    lexer.add_filter(SqlFilter())
    return highlight(raw_sql, lexer, formatters.TerminalFormatter())
