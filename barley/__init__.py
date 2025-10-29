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

@check50.check(compiles)
def test1():
    """handles a guess word quint"""
    check50.run("./barley").stdin("quint").stdout("Your guess is not in my list").exit(0)
