
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
	sub $sp, $sp, 48	# Make space for the locals
# Prologue ends
label0:
	lw $s0, 24($sp)
	lw $s1, 0($s0)
	l.s $f10, 0($s1)
	li.s $f12, 1.0
	add.s $f14, $f10, $f12
	mov.s $f10, $f14
	li.s $f12, 2.3
	li.s $f14, 3.4
	add.s $f16, $f12, $f14
	mov.s $f12, $f16
	add.s $f14, $f10, $f12
	mov.s $f10, $f14
	li.s $f12, 4.5
	add.s $f14, $f10, $f12
	mov.s $f10, $f14
	lw $s0, 24($sp)
	lw $s1, 0($s0)
	s.s $f10, 0($s1)
	lw $s0, 8($sp)
	lw $s1, 0($s0)
	lw $s0, 0($s1)
	lw $s1, 0($s0)
	lw $s0, 0($s1)
	lw $s1, 12($sp)
	lw $s2, 0($s1)
	lw $s1, 0($s2)
	lw $s2, 0($s1)
	add $s1, $s0, $s2
	move $s0, $s1
	li $s1, 4
	add $s2, $s0, $s1
	move $s0, $s2
	li $s1, 5
	li $s2, 3
	add $s3, $s1, $s2
	move $s1, $s3
	add $s2, $s0, $s1
	move $s0, $s2
	lw $s1, 4($sp)
	sw $s0, 0($s1)
	lw $s0, 4($sp)
	lw $s1, 0($s0)
	li $s0, 1
	add $s2, $s1, $s0
	move $s0, $s2
	lw $s1, 4($sp)
	sw $s0, 0($s1)
	j label1
label1:
	j epilogue_f1

# Epilogue begins
epilogue_f1:
	add $sp, $sp, 48
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
