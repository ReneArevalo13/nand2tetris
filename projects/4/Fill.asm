// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.


// @KBD: address that holds the keyboard value
// will have logic branches that handle the on and off states respectively



// have i be the row counter: 256 rows
// have j be the column counter: 32 columns of 16 bit chunks




(LOOP)

    @SCREEN
    D=A 
    @INDEX 
    M=D      // set pixel index to top left pixel

    @KBD     // read in the keyboard value
    D=M      // set the keyboard value

    @WHITE
    D;JEQ    // 0 if no input from keyboard set to white 
    D=-1     // set color to black (-1)


(WHITE)      // branch that determines whether white or black
    @COLOR
    M=D

(DRAW) 
    @INDEX 
    D=M 

    @KBD
    D=D-A 
    @LOOP
    D;JGE

    @COLOR    // retrieve what was stored in color 
    D=M

    @INDEX
    A=M 
    M=D    
    D=A+1
    @INDEX
    M=D 
    @DRAW
    0;JMP





