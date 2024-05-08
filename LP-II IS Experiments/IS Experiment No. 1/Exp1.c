#include<stdio.h>
#include<string.h>
int main()
{  	 char str[]="Hello World";
    	int i,len;
  	  len = strlen(str);
   	 printf("\n AND ing Operation with 127\t==>  ");
   	 for(i=0;i<len;i++)
  {
        	    printf("%c",str[i]&127);
 	   }
    printf("\n XOR ing Operation with 127\t==>  ");
    for( i=0;i<len;i++)
{
            	printf("%c",str[i]^127);
    }
    printf("\n OR ing Operation with 127\t==>  ");
    for(i=0;i<len;i++)
 {  
            printf("%c",str[i]|127);
    }
    printf("\n");
   return 0;
}
