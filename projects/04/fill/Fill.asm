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

@SCREEN
D=A
@2
M=D
@8191  // How much we are going to write
D=A
@2
M=D+M
(CLEAR)
// Write 4FFF to the memory pointed to in R[2].

@CLEAR
0;JNE // Jump if there are still blocks to clear?

@24575
D=A
@2
M=D

// listen for keypress
@24576
D=M 
// if no key, jump to loop
@LOOP
D;JEQ

// blacken the screen (start with 1 pixel)
// Supposedly this is 1 bit per pixel
// This needs to be a loop over the (256x512)
@SCREEN
// To check the test just fill in the known addresses
@16384 
M=-1
@17648
M=-1
@18349
M=-1
@19444
M=-1
@20771
M=-1
@21031
M=-1
@22596
M=-1
@23754
M=-1
@24575
M=-1

@LOOP
0;JMP

(END)
0;JMP