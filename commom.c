#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n,i=0,d,j,k;
    char c[100];
    scanf("%d",&n);
    struct str
    {
        char s[100];
    }a[10];
    for(i=0;i<n;i++)
    {
        scanf("%s",a[i].s);
    }

    for(i=0;i<n;i++)
    {

        for(j=0;a[i].s[j]!='\0';j++)
        {
            for(k=0;a[i+1].s[k]!='\0';k++)
            {
               if(a[i].s[j]==a[i+1].s[k])
               {
                   c[k]=a[i].s[k];
               }
            }
        }
    }
    puts(c);

    return 0;
}
