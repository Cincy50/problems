import check50
import check50.c

@check50.check()
def exists():
    """ziggy.c exist"""
    check50.exists("ziggy.c")

@check50.check(exists)
def compiles():
    """ziggy.c compiles"""
    check50.c.compile("ziggy.c", lcs50=True)

@check50.check(compiles)
def callAyZiggy():
    """Call Out to Ay Ziggy"""
    check50.run("./ziggy").stdin("Ay Ziggy").stdout("Zoomba!\n").stdin("q").exit(0)

@check50.check(compiles)
def callAyZiggyZoomba():
    """Call Out to Ay Ziggy Zoomba Zoomba Zoomba"""
    check50.run("./ziggy").stdin("Ay Ziggy Zoomba Zoomba Zoomba").stdout("Ay Ziggy Zoomba Zoomba Ze!\n").stdin("q").exit(0)

@check50.check(compiles)
def callAyZiggyOops():
    """Call Out to Garbage then Prompt again 'Enter the call: '"""
    check50.run("./ziggy")..stdin("Go vols!").stdout("Enter the call: ").stdin("Ay Ziggy Zoomba Zoomba Zoomba").stdout("Ay Ziggy Zoomba Zoomba Ze!\n").stdin("q").exit(0)

@check50.check(compiles)
def callZiggyQuits():
    """Make Sure program Ends"""
    check50.run("./ziggy").stdin("q").stdout("").exit(0)


