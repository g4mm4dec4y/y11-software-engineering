/* Filename: paperscissorsrockoneround.js

   Demonstrate how a one-round paper-scissors-rock game will work. */

/* Call the main function to get everything started. */
var counter, wins;

counter = 0;
wins = 0;

for (counter=0; counter < 3; counter++) {
	alert ('Wins:' + ' ' + wins);
	main();
}
alert ('Final wins:' + ' ' + wins);

/* Where it all happens. */
function main() {
	/* Declare and set variables for first use. */
	var i, available, choice;

	i = Math.floor(Math.random() * 3);
	available = new Array('paper', 'scissors', 'rock');

	/* Check to see what the user has input and whether it wins against the computer according to paper-scissors-rock
       rules or not. */
	
	choice = prompt ('Paper (p), scissors (s), or rock (r):','');

	if (choice == 'p') {
		if (available[i] == 'scissors') {
			alert ('You lose');
		} else if (available[i] == 'rock') {
			alert ('You win');
			wins+= 1;	
		}
	} else if (choice == 's') {
		if (available[i] == 'rock') {
			alert ('You lose');
		} else if (available[i] == 'paper') {
			alert ('You win');
			wins+= 1;
		}
	} else if (choice == 'r') {
		/* Now you have to complete this for ‘r’ or ‘rock’ */
		if (available[i] == 'paper') {
			alert ('You lose');
		} else if (available[i] == 'scissors') {
			alert ('You win');
			wins+= 1;
		}
	} 
}

