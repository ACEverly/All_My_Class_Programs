/*
Name: Mary-Rose Tracy 
ID#: 1001852753
*/
#include <stdio.h>

int main()
{
    //So there are 6 variables that the user needs to enter let's first declare those:
    int ISV, IEV, JSV, JEV, KSV, KEV; //Initial, S=starting E=Ending, V=Value
    //i's value
    //\n because I noticed on papar it looks more spaced than when I ran the code the first time.
    printf("\nEnter i's starting value ");
    scanf("%d",&ISV);
    
    printf("\nEnter i's ending value ");
    scanf("%d",&IEV);
    //j's value
    printf("\nEnter j's starting value ");
    scanf("%d",&JSV);
    
    printf("\nEnter j's ending value ");
    scanf("%d",&JEV);
    //k's value
    printf("\nEnter k's starting value ");
    scanf("%d",&KSV);
    
    printf("\nEnter k's ending value ");
    scanf("%d", &KEV);
    //little snippet for the code to go to the next line
    printf("\n");
    //Now here comes the loop
    //start with the I starting value and then the Ending Starting Value.
    for(int i=ISV; i<IEV; i++)
    {
        //second with the J starting value and the J ending value
        for(int j=JSV; j<JEV; j++)
        {
            //Finish with the K starting value and end w/ k ending value.
            for(int k=KSV; k<KEV; k++)
            {
                printf("*");
            }
            //I don't know how spaced you want the stars to be in betwen so I'm going to assume that it's just one space.
            printf("\n");
        }
        printf("\n\n\n");
    }
    return 0;
}


