class Baz():
    # this class was created to illustrate the scope of classes when imported.
    # note that, in scope.py, although this class is imported, the definition 
    # of another class named Baz overrides this definition. So, printing self.bar
    # from an instance of Baz() defined in scope.py would not print the int 4. 
    def __init__(self):
        self.bar = 4

    def scopeTest(self):
        print("inside instance of imported baz")
        print("printing bar")
        print(bar)
        print("printing self.bar")
        print(self.bar)
