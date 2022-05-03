import ply.lex as lex

from expressions import MDReExpressions

class InEmphasisLexer:

        tokens = [
                "LINKS",
                "ESCAPE_UNDERSCORE",
                "ESCAPE_STAR",
                "ESCAPE_TIDLE",
                "BOLD",
                "STRIKE",
                "QUOTED_TRIPLE",
                "QUOTED_DOUBLE",
                "QUOTED_SINGLE",
                "FOOT_NOTE"
                ]

        t_LINKS = MDReExpressions.LINK

        t_ESCAPE_UNDERSCORE = MDReExpressions.ESCAPE_UNDERSCORE
        t_ESCAPE_STAR = MDReExpressions.ESCAPE_STAR
        t_ESCAPE_TIDLE = MDReExpressions.ESCAPE_TIDLE

        t_BOLD = MDReExpressions.BOLD
        t_STRIKE = MDReExpressions.STRIKE

        t_QUOTED_TRIPLE = MDReExpressions.QUOTED_TRIPLE
        t_QUOTED_DOUBLE = MDReExpressions.QUOTED_DOUBLE
        t_QUOTED_SINGLE = MDReExpressions.QUOTED_SINGLE

        t_FOOT_NOTE = MDReExpressions.FOOT_NOTE

        def t_error(t):
                pass

        lexer = lex.lex()
