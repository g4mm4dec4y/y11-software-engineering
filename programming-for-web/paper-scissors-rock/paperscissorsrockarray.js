/* Filename: paperscissorsrockarray.js


   Demonstrate how the paper-scissors-rock array will work. */


/* Call the main function to get everything started. */
main();


/* Where it all happens. */
function main() {
	/* Declare and set variables for first use. */
	var rounds, available;


	available = new Array('paper', 'scissors', 'rock');


	/* Loop through the array printing out each option. */
	for (rounds = 0; rounds < 3; rounds++) {
		alert('available[' + rounds + '] = ' + available[rounds]);
		rounds = parseFloat(prompt("Enter number of rounds:" + " "));
	} 
}

