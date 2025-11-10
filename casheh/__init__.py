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
    check50.run("./casheh").stdin("2.50").stdin("5").stdout("I owe you: 2.50\n").stdout("Loonies: 2\n").stdout("Quarters: 2\n").stdout("Dimes: 0\n").stdout("Nickels: 0\n").exit(0)



@check50.check(compiles)
def test2():
    """handles a purchase of $3.03 with a $10 bill """
    check50.run("./casheh").stdin("3.03").stdin("10").stdout("I owe you: 6.97\n").stdout("Loonies: 7\n").stdout("Quarters: 0\n").stdout("Dimes: 0\n").stdout("Nickels: 0\n").exit(0)

