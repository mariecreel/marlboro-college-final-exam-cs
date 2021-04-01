/*
 * scope.js
 * This code was written to demonstrate how variable scope works in javascript.
 * In writing this code, I consulted various pages of the MDN javascript docs,
 * which I explicitly cite below. 
 *
 * Docs:
 * 	Closures https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
 * 	Var https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var
 *	a re-introduction to javascript
 *	https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
 *
 * Nick Creel - Apr 11, 2020 - MIT License
 */
let x = 1 // this is global and can be modified within the same scope
var y = 2 // this is global and can be modified within the same scope 
const z = 3 // this is global, but cannot be modified. 

function testScope(){
	if(x===1){
                let x = 4 // this does not change the value of the global to 4
		// but creates a new local variable called x that contains the 
		// value 4. if we had not used the let keyword in front of this
		// assignment, then the global variable would be changed. Unlike
		// var, declaring a local variable with the same name as
		// a global variable declared with let is possible. 
		console.log(x) // this should print 4.
	}else {
		console.log("value of x has changed")				
	}
	if(y===2){
		y = 5 // this changes the value of the global
		// note that we do not have to use something like the global 
		// statement in python to do this; this is just a feature of
		// how var is declared. if we attempted to declare var y = 5,
		// then var would be declared undefined both globally and locally
		// because var declarations are handled before any code is executed.
		// this creates a conflict between the var declared here and the 
		// var declared globally. 
	}else{
		console.log("value of y has changed")
	}

	var w = "this variable was declared inside of testScope()" 
	// because this is declared within a function scope,
	// this variable is contained within the function 
	// and not accessible outside of the local scope.
	console.log(x) // even though we created a new x, it is not accessible outside
	//              of the if statement in which it was defined.
	// 		this is different from python, which allows variables defined
	// 		within if statements to be used outside of those if statements. 
	console.log(y)
	console.log(z)
}

console.log(x)
console.log(y) // var does not change globally until testScope is run
console.log(z)
// console.log(w) if we ran this, we'd get a reference error, meaning w has not yet been named. 
// even though var is handled before the code is run, var declared within a function block 
// is still confined to that function. 

testScope()

console.log(x)
console.log(y)
console.log(z)
// console.log(w) if we ran this, we'd still get an error, even after running testScope, for
// the same reasons described above. 

// I will also demonstrate a closure, although I admit I have not seen closures before until
// this exam. My understanding of closures comes primarily from the MDN docs. I cite the 
// appropriate documentation at the top of this file. In any case, I wrote a closure similar
// to the closure in that documentation, though slightly different. 
// i discuss closures in more detail in problem1.txt
function legalName(last) {
	return function(first){
		return first + last
	}
}

var mahoney = legalName("Mahoney")
console.log(mahoney("jim")) // should print jimMahoney

