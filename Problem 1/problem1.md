#Algorithms and Programming Languages Exam: Problem 1
Marie Creel - Due April 17, 2020

Problem:

Describe and give specific examples of the various types of variable scope in
Python, Javascript, and C. Explain what's similar and what's different between
the languages.


Answer:

To start, I'll discuss the similarities and differences between the two languages
which I am most familiar with: Javascript and Python. I explore scope in each language
individually within the files scope.py, scope.js, and scope.c. In python, I also
had to create a separate file to explore global and nonlocal statements,
which is named nonlocal_and_global_statement.py, and to demonstrate import
scope, I created a module called baz.py. 

Note: I've listed all references I've used in the individual code files where
I used them, but I'll also list them at the bottom of this file. 

In python, the scope of a variable is typically confined to the block in which 
the variable was named. A block can be at the module level, the function level,
the class definition level, the instance level, the interpreted level, and even
within a call to eval() or exec(). 

Generally, variables are only accessible within the block they are defined or within
an block enclosed by the block they are defined in. For example, if I define a 
variable at the module level, then I can use that variable within a function that 
is also declared at the module level. 

For example:

```python
foo = 1
def bar():
	print(foo)

```
 if this code were run, then the value printed would be 1. 

However, just because a variable may be used in a block does not mean it may be
modified within a block. See the following example:

```python
foo = 1
def bar():
	foo = 2
	print(foo) # this prints 2
print(foo) # this prints 1
bar()
print(foo) # this prints 1
```

In order to modify the foo variable from within the bar function, we must
use the global statement for the foo variable within the bar function. This
tells the compiler that we want the value of the global foo to change when
we modify foo within bar.

```
foo = 1
def bar():
	global foo
	foo = 2
	print(foo) # this prints 2
print(foo) # this prints 1
bar()
print(foo) # this prints 2
```

Python also has a statement for nonlocal variables, which allows a function defined
within another function block to manipulate the value in the enclosing block without 
manipulating the value in the global block. I wrote an example of this in 
nonlocal_and_global_statement.py. 

In javascript, like python, there are multiple ways to declare a variable. 
For the most part, scope can be inferred from curly braces, but this is 
not always the case! 
variable scoping for variables declared with certain statements works 
differently, as each variable declaration statement gives that variable 
different properties.

First, there was the var declaration. Var is the oldest variable declaration statement
in Javascript, and it has unique variable scoping compared to  let and var. A var statement 
declared as a global variable can be modified from within any block that is enclosed 
by the global block, even without a global statement. See this example:

```javascript

var x = 1

function foo(){
        if(x===1){
                x = 2
        }
}
console.log(x) // this logs 1
foo()
console.log(x) // this logs 2

```

a variable declared using the let statement may only be used in the block in which it
was defined. You can find an example of this in scope.js at line 23, in the testScope
function. There, a variable that shares its name with  a globally scoped variable is
declared within an if statement. This newly named variable is only accessible within the 
if statement block. 

A const variable is also locally scoped to the block in which it's defined, but it 
cannot be modified. Attempting to modify a const variable, even if it's technically
in scope, will result in an error. 

Because a function in both languages has access to a variable defined in an enclosing
function / scope, both Javascript and Python can be used to write closures. Closures
are, in essence, functions that return other functions. What's important about closures 
is the fact that the returned function still has access to the variables defined in
the enclosing function that returned it. Closures might also be referred to as function
generators, but closures in particular refer to functions which return functions that
inherit the parent function's scope. 

Usually, once a function is called and finishes execution, the
python (or javascript) garbage collector (a memory management tool) cleans up the memory
by deleting the scope defined by an executed function once it is no longer needed. However, functions
returned by other functions may take local variables originally declared in the
outer function. In this case, the inner function can have its scope modified 
by the outer function before it's been executed.  

See this example:

```javascript

function name(last) {
	return function(first){
		return first + last
	}
}

var mahoney = name("Mahoney")
console.log(mahoney("jim")) //should print jimMahoney

```

The same can be done in Python, like so.

```python
def makeName(first):
    def _makeName(last):
        return first + last
    return _makeName

jim = makeName("jim")
print(jim("mahoney"))
```

Because Python and Javascript both treat functions as "first class citizens," passing
functions around is relatively simple, as they are treated like any other named 
variable until they are executed. The same cannot be said for C, where functions cannot
be passed around like other variables. 

From what I understand, closures are a particularly useful construct when dealing with 
events; For instance, if a web developer wanted to make a button that changed the color 
of a webpage, they might make a closure which takes a hex code as input and changes
the background color of the document; different version of this function could be made
for different colors and then made to be onClick events for the color changing buttons.
Like so:

```html
<html>
        <head>
                <script type="text/javascript">
                        function  makeColors(color){
                                return function(){
                                        document.body.style.background = color
                                }
                        }

                        let pink = makeColors("pink");
                        let blue = makeColors("blue");
                </script>                       
        </head>
        <body>
                <button onClick="pink()">Change Background To Pink</button>
                <button onClick="blue()">Change Background To Blue</button>
        </body>
</html>
```                           

C is a much more simplistic language than Javascript or Python in terms of scope;
In general, a variable may be accessed from the scope in which it's defined, 
as well as any scope enclosed within that initial scope. If a variable is 
named exactly the same as a variable that exists in a higher scope, then the variable 
in the most adjacent scope is used when called. For example, in the following code, when x is redefined within the main function, x > y evaluates to true, so the .out file
prints "max is 4"

```C
# include <stdio.h>

int max; /*maximum value out of x and y*/
int x = 2;
int y = 3;

main()
{
        x = 4;

        if(x > y)
                max = x;
        else
                max = y;
        printf("max is %d\n", max);
}
```

C programs may also contain named constants, which are similar in function to Javascript
const. In C, constant values are defined differently than variables, using #define statements,
and these define statements are located at the top of the file to indicate that they
are indeed different from variables. They can be used at any scope within the code 
once they are defined. Of course, a variable must be defined on an earlier line before
it may be used in a function regardless of whether or not it's within or without a 
certain scope. This is true of Python and C, while Javascript allows variables declared
with var to be "hoisted." This means that, as I mentioned, the variables are assigned 
values before the rest of the code runs. 

In C, when compiling code that must be used across multiple files, variables that
are to be used in multiple files must be marked with the extra keyword "extern" which
indicates to the compiler that these variables are located in another file. This would
typically be done in a header file. In Python, variables can be shared across files
using import statements, and in Javascript, variables may be shared in a number of ways;
The most common way I've done this is to include both files in the same .html page, 
but import/export statements are also used, generally to import all Javascript files for
a particular page into one index.js file. 


Sources Used:

All web sources were accessed on April 11, 2020.

* Python 3.8 Documentation:
	Execution Model https://docs.python.org/3.8/reference/executionmodel.html
    	Objects, Values, and Types https://docs.python.org/3.8/reference/datamodel.html
	Simple statements https://docs.python.org/3.8/reference/simple_stmts.html
* Javascript Documentation:
	Closures https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
 	Var https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var
 	a re-introduction to javascript
 	https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
* C Documentation:
	The C Programming Language, second edition, Brian W. Kernighan and Dennis M. Ritchie (1988)
* Stack overflow:
	nonlocal variables in python https://stackoverflow.com/questions/1261875/python-nonlocal-statement
