import check50
import check50.c

@check50.check()
def exists():
    """bingo.c exist"""
    check50.exists("bingo.c")

@check50.check(exists)
def compiles():
    """bingo.c compiles"""
    check50.c.compile("bingo.c", lcs50=True)
