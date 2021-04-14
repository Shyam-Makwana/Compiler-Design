/*

    The following program is a C code to generate Tokens. 
    @author="Shyam Makwana"

*/

#include<string.h>
#include<stdio.h>

void identify_token(char s[], int length)
{
    int i=0;
    while(i<length)
    {
        if (s[i] == 's')
        {
            i++;
            if (s[i] == 't' && s[i + 1] == 'r' && s[i + 2] == 'i' && s[i + 3] == 'n' && s[i + 4] == 'g') {
                printf("< Keyword , string>\n");
                i += 5;
            }
            else {
                i--;
                goto var;
            }
        }
        else if (s[i] == 'c') {
            i++;
            if (s[i] == 'h' && s[i+1] == 'a' && s[i+2] == 'r') {
                printf("< Keyword , char>\n");
                i += 3;
            }
            else {
                i--;
                goto var;
            }
        }
        else if (((int) s[i] >= 97 && (int) s[i] <= 122))
        {
            var: ;
            int flag_int=0;
            if((int)s[i]>=48 && (int)s[i]<=57)  flag_int=1;
            int j=i++;
            int len=1;
            while (((int) s[i] >= 65 && (int) s[i] <= 90) || ((int) s[i] >= 97 && (int) s[i] <= 122) || ((int)s[i]>=48 && (int)s[i]<=57)) {
                if((int)s[i]>=48 && (int)s[i]<=57)  flag_int=1;
                i++;
                len++;
            }
            if(flag_int==1 || len>3)    printf("Invalid ");
            printf("< ID , ");
            for(int k=j;k<i;k++)   printf("%c",s[k]);
            printf(" >\n");
        }
        else if (s[i] == '=') {
            printf("< Assop , = >\n");
            i++;
        }
        else if (s[i] == '+') {
            printf("< Relop , + >\n");
            i++;
        }
        else if (s[i] == '-') {
            printf("< Relop , - >\n");
            i++;
        }
        else if (s[i] == '?') {
            printf("< Relop , ? >\n");
            i++;
        }
        else if (s[i] == '<') {
            i++;
            if (s[i] == '-' && s[i+1] == '>') {
                printf("< Relop , <-> >\n");
                i += 2;
            }
            else {
                i--;
                goto invalid;
            }
        }
        else if ((int) s[i] == 32) {
            i++;
        }
        else if (s[i] == '\t') {
            i += 4;
        }
        else {
            invalid:
            printf("Invalid Token : %c\n",s[i++]);
        }
    }
}

int main()
{
    char s[] = " ";
    printf("\nEnter Program : ");
    gets(s);
    while(s[0]!='*')
    {
        identify_token(s, strlen(s));
        printf("\nEnter Program : ");
        gets(s);
    }
}
