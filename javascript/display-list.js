// Display list in Javascipt using while loop

let x = 1;

// Use process.stdout.write for no newline
 process.stdout.write("x = ["); 

while (x < 11) {
    process.stdout.write(`${x}`); // String Interpolation: `${x}`

    if (x < 10) {
       process.stdout.write(", ");
    }
    x++;
}

console.log("]");
