import check50
import check50.c

@check50.check()
def exists():
    """sort.c exist"""
    check50.exists("sort.c")

@check50.check(exists)
def compiles():
    """sort.c compiles"""
    check50.c.compile("sort.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles a static array of ints"""
    check50.run("./sort").stdout("12345678").exit(0)
