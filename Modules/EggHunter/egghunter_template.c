#include<stdio.h>
#include<string.h>

unsigned char payload[] =
"";

unsigned char egghuntr[] = 
"";

main()
{
	printf("Shellcode Payload Length:  %d\n", strlen(payload));
	int (*ret)() = (int(*)())egghuntr;
	ret();
}


