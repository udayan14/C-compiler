
	.data
global_d:	.word	0
global_eq:	.word	0

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
	addi $s0, $sp, 8
	sw $s0, 4($sp)
	j label1
label1:
	lw $s0, global_eq
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
	.text	# The .text assembler directive indicates
	.globl f2	# The following is the code
f2:
# Prologue begins
	sw $ra, 0($sp)	# Save the return address
	sw $fp, -4($sp)	# Save the frame pointer
	sub $fp, $sp, 8	# Update the frame pointer
	sub $sp, $sp, 12	# Make space for the locals
# Prologue ends
label2:
	lw $s0, 4($sp)
	lw $s1, 0($s0)
	li $s0, 1
	add $s2, $s1, $s0
	move $s0, $s2
	lw $s1, 4($sp)
	sw $s0, 0($s1)
	j label3
label3:
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
	sub $sp, $sp, 24	# Make space for the locals
# Prologue ends
label4:
	lw $s0, 8($sp)
	l.s $f10, 0($s0)
	li.s $f12, 4.5
	add.s $f14, $f10, $f12
	mov.s $f10, $f14
	# setting up activation record for called function
	lw $s0, 4($sp)
	lw $s1, 0($s0)
	sw $s1, -8($sp)
	s.s $f10, 0($sp)
	sub $sp, $sp, 12
	jal f # function call
	add $sp, $sp, 12 # destroying activation record of called function
	mov.s $f10, $f0 # using the return value of called function
	lw $s0, 8($sp)
	s.s $f10, 0($s0)
	j label5
label5:
	j epilogue_main

# Epilogue begins
epilogue_main:
	add $sp, $sp, 24
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
