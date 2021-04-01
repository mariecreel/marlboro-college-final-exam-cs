"""
nonlocal_and_global_statement.py

this code is meant to demonstrate the scope of variables declared
with nonlocal and global statements. In writing this code, I consulted
the python documentation for global and nonlocal statements. 

I had never used the nonlocal keyword before this exam, and I had trouble
determining how the keyword should be used just from reading the official
documentation on the simple statements page. I had written most of the code
for this, and I knew that using nonlocal required a nested function, but I 
was not sure whether I only had to declare bar at a global level, or if I
also needed to declare it within foo in order to use the nonlocal keyword
in quux. I consulted an answer on stackoverflow, after which I declared
a local version of bar within foo(). 

Stackoverflow:
    
    https://stackoverflow.com/questions/1261875/python-nonlocal-statement

docs: 
    simple statements https://docs.python.org/3.8/reference/simple_stmts.html

Nick Creel - Apr 11, 2020 - MIT License
"""

# nonlocal statements are not permitted at the module level,
# but a global statement may be used. 
baz = "baz" 
bar = "bar"
print(f"at module level before foo is called, baz is {baz}, bar is {bar}")
def foo():
    global baz
    bar = "foobar" # this is local
    baz = "foobaz" # because this was declared global, this modifies the value
                   # of the global baz variable on line 20. 
    print(f"in foo before quux(), bar is {bar} and baz is {baz}")
    def quux():
        nonlocal bar # this does not change bar to the global bar, but makes bar
                     # the bar as declared in foo(). changing this will not modify
                     # the global bar, but it will modify the bar in foo. 
                     # usually this kind of thing could only be done by returning
                     # a value and assigning that value to foo. I don't use 
                     # nonlocal keywords often, but it seems they could get
                     # confusing and difficult to debug due to the side effects. 
        print(f"just declared bar nonlocal in quux, bar is {bar}")
        bar = "quuxbar" # this changes the value of bar in foo
        baz = "quuxbaz" # this is local, will not change the value of foo or global
        print(f"in quux, bar = {bar} and baz = {baz}")
    quux()
    print(f"in foo after quux(), bar = {bar} and baz = {baz}") 
    # the value of bar should still be quuxbar
foo()
print(f"at module level after foo(), bar={bar} and baz={baz}")

