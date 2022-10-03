# A instruction
Set the A register to a value

`@value`

Value is non-negative integer

# C instruction (control)

`dest = comp; jump`

## jump
null
JGT
JEQ
JGE
JLT
JNE
JLE
JMP

## comp


## destination
|code|Description|
|---|---|
|null|Not stored|
|M|RAM[A]|
|D|D register|
|MD|RAM[A] and D register|
|A|A register|
|AM|A register and RAM[A]|
|AD|A register and D Register|
|AMD|A register, RAM[A], and D Register|