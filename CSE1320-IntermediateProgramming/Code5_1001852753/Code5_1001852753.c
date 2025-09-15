//Name: Mary-Rose Tracy 
//ID#:1001852753
#include <stdio.h>
#include <stdlib.h>
#include "GameLib.h"
#include <string.h>

int main()
{
    //Let's distinguish the ChosenPhrase used,
    //the dashPhrase 
    //& the upperphrase, and put it in MAX_INPUT.
    char ChosenPhrase[MAX_INPUT];
    char DashedPhrase[MAX_INPUT];
    char UpperPhrase[MAX_INPUT];
    int numstrikes = 0; //set number of strikes to zero
    char Dash = '-'; //make the dash = '-'
    //in the start of the game we choose a phrase
    StartGame(ChosenPhrase);
    DashIt(ChosenPhrase, DashedPhrase);

    for( int i = 0; i < strlen(ChosenPhrase); i++) //we need to increment the strlen
    {
        UpperPhrase[i] = toupper(ChosenPhrase[i]);
    }

    do
    {
        if (GuessALetter(ChosenPhrase, DashedPhrase, UpperPhrase) == 0)
        {
            numstrikes++;
            printf("Strikes %d\n", numstrikes);
        }
    }

    while (strchr(DashedPhrase, Dash) != NULL && numstrikes < STRIKES);

    if(numstrikes < STRIKES)
    {
        printf("You figured it out!!\n");
        printf("The phrase was %s\n\n", ChosenPhrase);
        printf("YOU WIN!!!!\n");
    }

    else
    {
        printf("3 STRIKES - YOU'RE OUT!!\n");
        printf("Game over\n");
    }

    return 0;
}

