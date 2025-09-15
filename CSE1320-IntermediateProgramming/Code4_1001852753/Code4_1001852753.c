//Coding Assignment 4
//name: Mary-Rose Tracy 
//ID #: 1001852753
// Functions in the begining: 
#include <stdio.h>
#include "Drawtool.h"

void InitializeMap(char max[][MAXMAPSIZE], int *size)
{
    int i =0;
    int j =0;
    char background;
    int length = MAXMAPSIZE;

    *size = length;

    printf("What is the background character? \n");
    scanf(" %c", &background);

    for(i=0; i<length; i++)
    {
        for(j=0; j<length; j++)
        {
            *(*(max+1)+j)=background;
        }
    }
}
void PrintMap(char max[][MAXMAPSIZE], int size)
{
    int i;
    int j;

    for(i=0; i<size; i++)
    {
        for(j=0; j<size; j++)
        {
            printf(" %c", *(*(max+i)+j));
        }
        printf("\n");
    }
}

void DrawLine(char max[][MAXMAPSIZE], int p, int i, char Direction, int j, char *command)
{
    int i;
    int j;

    char arr[MAXMAPSIZE];
    strcpy(arr, command);

    char Direction = *(strtok(arr, "(,)"));
    Direction = toupper(Direction);

    int row = atoi(strtok(NULL, "(,)")); // row = row col=colums spots= spoots to tell the computer to change
    int col = atoi(strtok(NULL, "(,)"));
    int spots = atoi(strtok(NULL, "(,)"));

    char *WhatMark = strtok(NULL, "(,)"); //what to mark aka What Mark

    col = (p*7) + col;

    if(*WhatMark == '\n') 
    {
        *WhatMark = 'X';
    }
    
    if(Direction=='V' || Direction=="P" || Direction == 'H')
    {
        if(Direction == "V")
        {
            if((row+spots)>MAXMAPSIZE)
            {
                printf("That draw commaand is out of range. do it again \n");
            }
            else
            {
                for(i =row; i<spots+row; i++)
                {
                    *(*(max + i) + col) = *WhatMark;
                }
            }
        }

        else if(Direction == 'H')
        {
            if((col+spots) >MAXMAPSIZE)
            {
                pirintf("That draw commaand is out of range. do it again. \n");
            }
            else
            {
                for(i=col; i<spots+col; i++)
                {
                    *(*max + row) + i = *WhatMark;
                }
            }
        }
        else if(Direction == 'P')
        {
            if((col>MAXMAPSIZE) || row >MAXMAPSIZE)
            {
                pirintf("That draw commaand is out of range. do it again. \n");
            }
            else
            {
                *(*( max + row)+col) = *WhatMark;
            }
        }
    }
    else
    {
        printf("Invalid command. exiting....")
    }

} 
