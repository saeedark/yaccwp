# Generated from: c_test/while.c
# Generated at: 2021-06-25 19:55:44.718913
.data
lbl3: .asciiz "calculation completed."
.text

main:
addi $sp, $sp, -8
sw $ra, 0($sp)
li $t0,0
sw $t0, 4($sp)
lbl2:
lw $t0, 4($sp)
li $t1,10
bge $t0, $t1, lbl1
lw $t0, 4($sp)
addi $t0, $t0, 1
sw $t0, 4($sp)
j lbl2
lbl1:
lw $t0, 4($sp)
li $t2,2
mul $t1, $t0, $t2
sw $t1, 4($sp)
la $a0, lbl3
li $v0, 4
syscall
lw $ra, 0($sp)
addi $sp, $sp, 8
li $v0 10 #prgoram finished call terminate
syscall

