@2
M=0  // Set R2 to 0, this is where we put our answer
(LOOP)
@0
D=M
@1
D=D+A
@0
M=M-1  // WRONG. Don't modify R0 and R1.
@LOOP
0;JGT
(END)
@2
M=
@END
0;JMP