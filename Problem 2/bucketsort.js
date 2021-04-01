/*
bucketsort.js
implementation of bucket sort, in an attempt to partially answer this question:
	Implement, numerically test, and explain two different sorting
    algorithms with different O() behaviors on randomly chosen
    lists of numbers with various sizes n. Use two different
    programming languages and coding styles. Show graphically
    that the expecected performance is consistent with your
    numerical experiments.

the bucket sort is defined as follows:

Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

from Bucket Sort, wikipedia. https://en.wikipedia.org/wiki/Bucket_sort

I did not consult the wikipedia pseudocode for this, as the bucket sort definition is
fairly intuitive.

Nick Creel - Apr 13, 2020 - MIT License
*/
const numbuckets = 1000000
function randInt(max){
/*
this function takes an integer as input and returns a random integer between
0 and the number provided. This code is exactly the code for a random integer
from the MDN docs for Math.random().
See this document for more:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
*/
	return Math.floor(Math.random() * Math.floor(max))
}

function generateNLengthArray(n){
/*
this function takes an integer as input and returns an array of randomly chosen
numbers where the length is equal to the integer given as an argument.
*/
	let nArray = []
	for(let i=0; i<n; i++){
		nArray.push(randInt(numbuckets))
	}
	return nArray
}

function makeMArrays(n, m){
/* this function takes two integers as input and returns an array of arrays. the outermost
array is length m, while all the inner arrays are length n.
*/
	let mArray = []
	for(let i=0; i<m; i++){
		mArray.push(generateNLengthArray(n))
	}
	return mArray
}

function bucketSort(array){
/*
this function takes an array as input and returns a tuple where the
0th element is the original list with values sorted from least to greatest, and the
1st element is a float representation of the runtime in milliseconds.
*/
	let startTime = Date.now()
	let buckets = []
	//console.log("array is", array)
	let max = Math.max(...array) // spread operator needed to find max of array. makes
								 //  individual arguments. so if array == [1,2,3],
								 // ...array = 1,2,3

	for(let i=0; i < (max+1); i++){      // make buckets....this is the silliest way.
								   // probably will slow down at high lengths
		buckets.push([])
	}


	for(let i=0; i<array.length; i++){ // each number just has its own little bucket
		index = array[i] 		   // no index errors!

		//console.log(index)
		buckets[index].push(array[i]) // this has to be under a different loop so no und.
	}

	let sortedArray = []
	for(let i=0; i<buckets.length; i++){ // unpack buckets into a single array
		if(buckets[i].length>0){
			for(j=0; j<buckets[i].length; j++){
				//console.log(buckets[i][j])
				sortedArray.push(buckets[i][j])
			}
		}
	}
	let endTime = Date.now()
	let runTime = (endTime - startTime)
	//console.log("runTime",runTime)
	//console.log("sortedArray[sortedArray.length-1]",sortedArray[sortedArray.length-1])
	return [sortedArray, runTime]
}

function main(){
	let runtimes =[] // list of list of runtimes
	let array10s = makeMArrays(10, 10)
	let array30s = makeMArrays(30, 10)
	let array100s = makeMArrays(100, 10)
	let array300s = makeMArrays(300, 10)
	let array1000s = makeMArrays(1000, 10)
	let	array3000s = makeMArrays(3000, 10)
	let array10000s = makeMArrays(10000, 10)
	let	array30000s = makeMArrays(30000, 10)
	let	array60000s = makeMArrays(60000, 10)
	let	array80000s = makeMArrays(80000, 10)
	let	array100000s = makeMArrays(100000, 10) // this is as high as i can get without
											   // call stack overflow error
	//console.log(array30000s[0].length)
	let allArrays = [array10s, array30s, array100s, array300s, array1000s, array3000s, array10000s, array30000s, array60000s, array80000s, array100000s]

	const sizes = [10,30,100,300,1000,3000,10000,30000,60000, 80000, 100000]
	let count = 0
	for(let i=0; i<allArrays.length; i++){
		let runtime = [] // all runtimes for one size
		for(let j=0; j<allArrays[i].length; j++){
			runtime.push(bucketSort(allArrays[i][1]))
		}
		runtimes.push([sizes[count], runtime])
		count += 1
	}
	// I got help on CSV exports via this stackoverflow article
	// https://stackoverflow.com/questions/14964035/how-to-export-javascript-array-info-to-csv-on-client-side
	let csvContent = ""
	rows = []
	for(let i=0; i<runtimes.length; i++){
		let size = runtimes[i][0]
		for(let j=0; j<runtimes[i].length; j++){
			for(let k=0; k<runtimes[i][j].length; k++){
 				rows.push([size.toString(), runtimes[i][j][k][1].toString(), numbuckets.toString()]) // get runtime!
			}
		}
	}
	//console.log("rows", rows)

	for(let row = 0; row < rows.length; row++){
		csvContent += rows[row].join(",")
		csvContent += "\r\n"
	}
	console.log(csvContent) //instead of I/O, do "node bucketsort.js > bucketsort.csv"
}

main()


