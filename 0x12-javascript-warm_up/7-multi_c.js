#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2]);
if (isNaN(num)){
	console.log("Missing number of occurrences");
}else{
	let x = 0;
	while (x < num){
		console.log("C is fun");
		x++;
	}
}
