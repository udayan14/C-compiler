
	.data
global_d:	.word	0

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
	lw $s0, 4($sp)
	move $v1, $s0 # move return value to $v1
	j epilogue_f

# Epilogue begins
epilogue_f:
	add $sp, $sp, 16
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
	.text	# The .text assembler directive indicates
	.globl f2	# The following is the code
f2:
# Prologue begins
	sw $ra, 0($sp)	# Save the return address
	sw $fp, -4($sp)	# Save the frame pointer
	sub $fp, $sp, 8	# Update the frame pointer
	sub $sp, $sp, 12	# Make space for the locals
# Prologue ends
label1:
	lw $s0, global_d
	move $v1, $s0 # move return value to $v1
	j epilogue_f2

# Epilogue begins
epilogue_f2:
	add $sp, $sp, 12
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
	sub $sp, $sp, 48	# Make space for the locals
# Prologue ends
label2:
	lw $s0, 20($sp)
	sw $s0, 16($sp)
	lw $s0, 32($sp)
	sw $s0, 16($sp)
	lw $s0, 28($sp)
	sw $s0, 24($sp)
	lw $s0, 36($sp)
	sw $s0, 24($sp)
	lw $s0, 32($sp)
	sw $s0, global_d
	lw $s0, 20($sp)
	lw $s1, 40($sp)
	sw $s0, 0($s1)
	lw $s0, 8($sp)
	lw $s1, 0($s0)
	lw $s0, 0($s1)
	lw $s1, 0($s0)
	lw $s0, 20($sp)
	sw $s1, 0($s0)
	lw $s0, 28($sp)
	l.s $f10, 0($s0)
	lw $s0, 4($sp)
	lw $s1, 0($s0)
	lw $s0, 0($s1)
	s.s $f10, 0($s0)
	lw $s0, 24($sp)
	l.s $f10, 0($s0)
	lw $s0, 36($sp)
	l.s $f12, 0($s0)
	add.s $f14, $f10, $f12
	mov.s $f10, $f14
	# setting up activation record for called function
	lw $s0, 12($sp)
	lw $s1, 0($s0)
	l.s $f12, 0($s1)
	s.s $f12, -8($sp)
	s.s $f10, 0($sp)
	sub $sp, $sp, 16
	jal f2 # function call
	add $sp, $sp, 16 # destroying activation record of called function
	move $s0, $v1 # using the return value of called function
	sw $s0, 16($sp)
	j label3
label3:
	j epilogue_main

# Epilogue begins
epilogue_main:
	add $sp, $sp, 48
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
