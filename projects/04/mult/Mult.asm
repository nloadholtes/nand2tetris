@2
M=0  // Set R2 to 0, this is where we put our answer
// Set R3 to be the value in R2
@2
D=M
@3
M=0
// Loop
(LOOP)
@0
D=M
@2
D=D+A
@3  // R3 is our counter, decrement it by 1
M=M-1
@LOOP
0;JGT
(END)
@END
0;JMP