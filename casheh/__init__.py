#
import check50
import check50.c

@check50.check()
def exists():
    """casheh.c exist"""
    check50.exists("casheh.c")

@check50.check(exists)
def compiles():
    """casheh.c compiles"""
    check50.c.compile("casheh.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles a purchase of $2.50 with a $5 bill """
    check50.run("./casheh").stdin("quint").stdout("Your guess is not in my list").exit(0)
