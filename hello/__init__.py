@check50.check()
def test1():
  """responds to name walkdo"""
  check50.run("./hello").stdin("Waldo").stdout("Hello, Waldo").exit(0)
