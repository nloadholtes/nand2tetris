// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


(LOOP)
// clear memory

// listen for keypress
@24576
D=M 
// if no key, jump to loop
@LOOP
D;JEQ

// blacken the screen (start with 1 pixel)
// This needs to be a loop over the (256x512)
@2
M=16384

@SCREEN
M=1

@LOOP
0;JMP