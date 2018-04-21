
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
	li $s0, 6
	li $s1, 7
	slt $s2, $s1, $s0
	move $s0, $s2
	li $s1, 5
	li $s2, 4
	slt $s3, $s2, $s1
	move $s1, $s3
	li $s2, 7
	li $s3, 8
	slt $s4, $s3, $s2
	move $s2, $s4
	and $s3, $s1, $s2
	move $s1, $s3
	and $s2, $s0, $s1
	move $s0, $s2
	bne $s0, $0, label3
	j label4
label3:
	lw $s0, 16($sp)
	lw $s1, 0($s0)
	li $s0, 1
	add $s2, $s1, $s0
	move $s0, $s2
	lw $s1, 16($sp)
	sw $s0, 0($s1)
	j label4
label4:
	j epilogue_main

# Epilogue begins
epilogue_main:
	add $sp, $sp, 48
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
