// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.
// sum = 0
// while(count < R1) {
//     sum += R0
//}

//// Replace this comment with your code.

    @R0      // register 0 value
    D = M    // D set to value at register 0

    @R2      // output register
    M = 0    // initialize to 0

    @count   // set a counter variable
    M = 1    // count = 1

    @sum     // running sum
    M = 0    // initialize to 0 

(LOOP)
    @count
    D = M 
    @R0
    D = D - M
    @END
    D;JGT    // if (count - R0) > 0 goto END
    @R1
    D = M    // R value
    @R2
    M = D+M  // sum = sum + R1 
    @count 
    M = M+1  // increment count by 1
    @LOOP
    0;JMP    // goto LOOP 
(END)
    @END
    0;JMP    // infinite loop to terminate





