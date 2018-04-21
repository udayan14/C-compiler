
	.data
global_a1:	.space	8
global_a2:	.word	0
global_a3:	.word	0
global_a4:	.word	0
global_d:	.word	0
global_d1:	.word	0
global_d2:	.word	0

	.text	# The .text assembler directive indicates
	.globl f	# The following is the code
f:
# Prologue begins
	sw $ra, 0($sp)	# Save the return address
	sw $fp, -4($sp)	# Save the frame pointer
	sub $fp, $sp, 8	# Update the frame pointer
	sub $sp, $sp, 16	# Make space for the locals
# Prologue ends
label0:
	la $s0, global_d
	lw $s1, 4($sp)
	sw $s0, 0($s1)
	j label1
label1:
	lw $s0, global_a2
	l.s $f10, 0($s0)
	mov.s $f0, $f10 # move return value to $f0
	j epilogue_f

# Epilogue begins
epilogue_f:
	add $sp, $sp, 16
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
