
	.data
global_a:	.word	0
global_d:	.word	0
global_fff:	.word	0

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
	li.s $f10, 6.4
	li.s $f12, 7.3
	c.le.s $f10, $f12
	bc1f L_CondFalse_0
	li $s0, 1
	j L_CondEnd_0
L_CondFalse_0:
	li $s0, 0
L_CondEnd_0:
	move $s1, $s0
	bne $s1, $0, label3
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
	li.s $f10, 6.4
	li.s $f12, 7.3
	c.le.s $f12, $f10
	bc1f L_CondFalse_1
	li $s0, 1
	j L_CondEnd_1
L_CondFalse_1:
	li $s0, 0
L_CondEnd_1:
	move $s1, $s0
	bne $s1, $0, label5
	j label6
label5:
	lw $s0, 16($sp)
	lw $s1, 0($s0)
	li $s0, 1
	add $s2, $s1, $s0
	move $s0, $s2
	lw $s1, 16($sp)
	sw $s0, 0($s1)
	j label6
label6:
	li.s $f10, 6.4
	li.s $f12, 7.3
	c.eq.s $f10, $f12
	bc1f L_CondFalse_2
	li $s0, 1
	j L_CondEnd_2
L_CondFalse_2:
	li $s0, 0
L_CondEnd_2:
	move $s1, $s0
	li.s $f10, 6.4
	li.s $f12, 7.2
	c.lt.s $f12, $f10
	bc1f L_CondFalse_3
	li $s0, 1
	j L_CondEnd_3
L_CondFalse_3:
	li $s0, 0
L_CondEnd_3:
	move $s2, $s0
	and $s0, $s1, $s2
	move $s1, $s0
	bne $s1, $0, label7
	j label8
label7:
	lw $s0, 16($sp)
	lw $s1, 0($s0)
	li $s0, 1
	add $s2, $s1, $s0
	move $s0, $s2
	lw $s1, 16($sp)
	sw $s0, 0($s1)
	j label8
label8:
	li.s $f10, 6.4
	li.s $f12, 7.3
	c.eq.s $f10, $f12
	bc1f L_CondTrue_4
	li $s0, 0
	j L_CondEnd_4
L_CondTrue_4:
	li $s0, 1
L_CondEnd_4:
	move $s1, $s0
	bne $s1, $0, label9
	j label10
label9:
	lw $s0, 16($sp)
	lw $s1, 0($s0)
	li $s0, 1
	add $s2, $s1, $s0
	move $s0, $s2
	lw $s1, 16($sp)
	sw $s0, 0($s1)
	j label10
label10:
	j epilogue_main

# Epilogue begins
epilogue_main:
	add $sp, $sp, 48
	lw $fp, -4($sp)
	lw $ra, 0($sp)
	jr $ra	# Jump back to the called procedure
# Epilogue ends
