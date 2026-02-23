#
import check50
import check50.c

@check50.check(exists)
def exists():
    """wordle.c exist"""
    check50.exists("wordle.c")

@check50.check(compiles)
def compiles():
    """wordle.c compiles"""
    check50.c.compile("wordle.c", lcs50=True)
