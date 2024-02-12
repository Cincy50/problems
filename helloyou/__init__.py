import check50
import check50.c

@check50.check()
def exists():
    """helloyou.c exists"""
    check50.exists("helloyou.c")

@check50.check(exists)
def compiles():
    """helloyou.c compiles"""
    check50.c.compile("helloyou.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./helloyou").stdin("Moose").stdout("Hello, Moose").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./helloyou").stdin("SingerBee").stdout("Hello, StingerBee").exit()
