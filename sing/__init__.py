import check50
import check50.c

@check50.check()
def exists():
    """loops.c exist"""
    check50.exists("loops.c")

@check50.check(exists)
def compiles():
    """loops.c compiles"""
    check50.c.compile("loops.c", lcs50=True)
