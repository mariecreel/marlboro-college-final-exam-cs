"""
scope.py

the code in this file is meant to demonstrate how variable scope 
works in python 3.8. When writing this code, I referred to the Python 3.8
documentation to ensure that I was using the correct technical vocabulary
in my own documentation, but all code written is my own. 

Doc pages I referred to:
    Execution Model https://docs.python.org/3.8/reference/executionmodel.html
    Objects, Values, and Types https://docs.python.org/3.8/reference/datamodel.html

Nick Creel - Apr 11, 2020 - MIT License
"""
# the scope of a code block or variable is determined when the block/var is named
from baz import Baz
# because Baz is imported at the module level, it is globally defined. 
bar = 2 
# bar is a global variable because it is defined within module block
# all function and class definitions at the module level are also global
class Baz():
    # because this class is defined after we imported another class named Baz,
    # this particular definition will be resolved instead of the imported Baz. 
    # see the scopeTest method and the output of this file when run to confirm.
    def __init__(self):
        self.bar = 3 
        #not only is this bar local, but can only be accessed as attr of a named
        #instance of this class, because it is attached to the self keyword. 
        #in addition, this variable can be changed in a particular instance,
        #but that will not change the value of the variable in the class defintion.
        # variables declared using the "self." prefix is known as
        # an instance attribute. 
    def scopeTest(self): 
        # this method is a class attribute.
        # this means that it is shared across all instances of the class.
        # unlike an instance attribute, a class attribute may be called 
        # by calling through the class (Baz().scopeTest()) or by calling
        # through an instance (baz = Baz(), baz.scopeTest()). 
        # the defintion of a class instance may be changed at an instance
        # level (so, a particular instance could change the function of scopeTest),
        # but the original class definition would remain unaltered. 
        # even though this method may be called without creating an instance,
        # it cannot be called as a function without referencing the class
        # for example, simply calling scopeTest() without Baz(). or an instance
        # would result in a NameError. 
        print("inside scopeTest function scope")
        print("printing bar")
        print(bar)
        
        # because there's a variable named bar in the nearest enclosing scope, 
        # this will always print the global bar rather than, say, a local bar
        # defined at the same scope as an instance of this class. 
        # see the foo() fxn for an example.
        # HOWEVER, see the following for an example where the global would
        # not be resolved: 
        # bar = 5 
        # if the above line were uncommented, there would be an error, namely
        # an UnboundLocalError, as the print(bar) statement above would be called
        # before bar was assigned in local scope. In this case, the executed code 
        # cannot just resolve the global bar, as the local bar is within the same
        # scope, and bar is not preceded by a global or nonlocal statement. . 
        print("printing self.bar")
        print(self.bar)

def foo():
    baz = Baz()
    print("executing foo()")
    bar = 1 # this is a local variable bound to the function scope
            # this variable may only be used within function scope,
            # and it does not reassign the global bar variable. 
    print(bar)
    
    baz.bar = 6
    print("printing baz.scopeTesi() inside foo()")
    baz.scopeTest()
    print("printing Baz().scopeTest() inside foo()")
    Baz().scopeTest()
    print("exiting foo() scope")
    
foo() # should print 1
print("printing bar outside of foo()")
print(bar) # should print 2
