@2
M=0  // Set R2 to 0, this is where we put our answer
// Set R3 to be the value in R2
@1
D=M
@3
M=D
// Loop
(LOOP)
@3  // R3 is our counter, decrement it by 1
D=M
@END
D=D-1  // Decrement only if > 0
0;JEQ  // Jump to the end if we are less than 0
@0
D=M
@2  // Perform the addition
M=D+M
@LOOP
0;JMP  // Jump back to the top of loop
(END)
@END
0;JMP

//
//
//

// Init RAM[3] to RAM[1]. This is the counter
@1
D=M
@3
M=D

// Set top-of-loop marker
// If @3 is less than or equal to 0, jump to end
// Set RAM[2] = RAM[2] + RAM[0]
// Decrement @3
// JMP to LOOP

// set END marker
// JMP TO END (infinite loop)