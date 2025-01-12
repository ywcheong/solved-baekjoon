#include<stdio.h>
main()
{
    int t, s = 1;
    scanf("%d",&t);

    int swap1, swap2;
    for (int k =0; k < t; k++)
    {
        scanf("%d %d", &swap1, &swap2);
        
        if(swap1 == s)
            s = swap2;
        else if(swap2 == s)
            s = swap1;
    }
    printf("%d", s);
}