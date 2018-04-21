
	.data
global_a:	.word	0
global_a1:	.word	0
global_a2:	.space	8
global_a3:	.word	0
global_b:	.word	0
global_b2:	.word	0

	.text	# The .text assembler directive indicates
	.globl f1	# The following is the code
f1:
# Prologue begins
	sw $ra, 0($sp)	# Save the return address
	sw $fp, -4($sp)	# Save the frame pointer
	sub $fp, $sp, 8	# Update the frame pointer
	sub $sp, $sp, 40	# Make space for the locals
# Prologue ends
label0:
	lw $s0, 24($sp)
	lw $s1, 0($s0)
	move $v1, $s1 # move return value to $v1
	j epilogue_f1

# Epilogue begins
epilogue_f1:
	add $sp, $sp, 40
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
	.text	# The .text assembler directive indicates
	.globl main	# The following is the code
main:
# Prologue begins
	sw $ra, 0($sp)	# Save the return address
	sw $fp, -4($sp)	# Save the frame pointer
	sub $fp, $sp, 8	# Update the frame pointer
	sub $sp, $sp, 20	# Make space for the locals
# Prologue ends
label1:
	# setting up activation record for called function
	lw $s0, global_a
	sw $s0, -20($sp)
	lw $s0, global_a3
	l.s $f10, 0($s0)
	s.s $f10, -12($sp)
	lw $s0, global_a3
	l.s $f10, 0($s0)
	s.s $f10, -4($sp)
	lw $s0, global_a
	lw $s1, 0($s0)
	sw $s1, 0($sp)
	sub $sp, $sp, 24
	jal f1 # function call
	add $sp, $sp, 24 # destroying activation record of called function
	move $s0, $v1 # using the return value of called function
	sw $s0, 4($sp)
	j label2
label2:
	j epilogue_main

# Epilogue begins
epilogue_main:
	add $sp, $sp, 20
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
