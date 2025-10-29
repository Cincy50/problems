import check50
import check50.c

@check50.check()
def exists():
    """barley.c exist"""
    check50.exists("barley.c")

@check50.check(exists)
def compiles():
    """barley.c compiles"""
    check50.c.compile("barley.c", lcs50=True)
