//Name: Mary-Rose Tracy 
//ID#: 1001852753
//Step 1: Literally #include everything since there is so many moving parts to this bingo thing, it's not even funny.
#include<stdio.h>
#include<time.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>

//First we print the Bingo card= void because it's just like there & done
void PrintBCard(int *arr,int S) //Need to do a pointer for the arr to tell the computer hey this ish needs to be focused on
{
    printf("\n\n    B       I       N       G       O    ");
    printf("\n-----------------------------------------\n");
    for(int i = 0; i<S; i++)//size of the box
    {
        for(int j = 0; j< S; j++)
        {
            int value = *((arr + i * 5) + j);
            if(value == 0)
            {
                printf("|   X   ");//says to turn it to x
            } 
            else
            {
                printf("|  %-5d", *((arr + i * 5) + j));
            }
        }
        printf("|\n-----------------------------------------\n");
    }
}

char getRandomCol() //I implemented this afterward which I regret because now I confuse myself
{
    char alphabet[5] = {'B', 'I', 'N', 'G', 'O'};
    return alphabet[rand() % 5];
}

int ifNExists(int *arr,int S, int target, char chosenCol)
{
    int col; //only column can be random Letter BINGO
    if(chosenCol == 'B')
        col = 0;
    else if(chosenCol == 'I')
        col = 1;
    else if(chosenCol == 'N')
        col = 2;
    else if(chosenCol == 'G')
        col = 3;
    else
        col = 4;
    for(int i = 0; i<S; i++)
    {
        if (*((arr + i * 5) + col) == target)
        {
            *((arr + i * 5) + col) = 0;
            return 1; 
        }
    }
    return 0;
}
//Need to make is row complete and iscolumncompleted a separate function.
int isRowCompleted(int arr[][5],int S)
{
    for(int i = 0; i<S; i++)
    {
        if (arr[i][0] == 0 && arr[i][1] == 0 && arr[i][2] == 0 && arr[i][3] == 0 && arr[i][4] == 0)
            return 1;
    }
    return 0;
}

int isColumnCompleted(int arr[][5], int S)
{
    for (int i = 0; i < S; i++)
    {
        if (arr[0][i] == 0 && arr[1][i] == 0 && arr[2][i] == 0 && arr[3][i] == 0 && arr[4][i] == 0)
            return 1;
    }
    return 0;
}
//make that main
int main()
{
    srand((unsigned int)time(0)); //of course time is set to NULL or zero.
    int bingo[5][5],S = 5;
    for(int i = 0; i < S; i++)
    {
        for(int j = 0; j<S; j++)
        {
            if (j == 0)
            {
                bingo[i][j] = (rand()%15) + 1;
            }
            else if(j == 1)
            {
                bingo[i][j] = (rand() %15) + 16;
            }
            else if(j == 2)
            {
                bingo[i][j] = (rand() %15) + 31;
            }
            else if(j == 3)
            {
                bingo[i][j] = (rand() %15) + 46;
            }
            else
            {
                bingo[i][j] = (rand() %15) + 61;
            }
        }
    }
    int chosenArray[75];
    int leftNum = 75;
    int chosenNum;
    int chosenIndex;
    char choice;
    char chosenCol;
    for(int i = 0; i< 75; i++)
    {
        chosenArray[i] = i+1;
    }
    while(isRowCompleted(bingo,S) == 0 && isColumnCompleted(bingo,S) == 0)
    {
        PrintBCard((int *)bingo,S);
        chosenIndex = rand() % leftNum;
        chosenNum = chosenArray[chosenIndex];
        chosenCol = getRandomCol();
        chosenArray[chosenIndex] = chosenArray[leftNum];
        --leftNum;
        printf("\n\nThe chosen number is: %c%d\n", chosenCol, chosenNum);
        printf("Do you have the number? (Y/N): ");
        scanf(" %c",&choice);
        if((choice == 'y' || choice == 'Y') && ifNExists((int *)bingo, S,chosenNum, chosenCol) == 1)
        {
            printf("\n");
        }
        else if ((choice == 'n' || choice == 'N') && ifNExists((int *)bingo, S, chosenNum, chosenCol) == 1)
        {
            printf("\n");
        }
        else if ((choice == 'y' || choice == 'Y') && ifNExists((int *)bingo, S, chosenNum, chosenCol) == 0)
        {
            printf("\nThat value is not on your BINGO card - are you trying to cheat??");
        }
        else
        {
            printf("\n");
        }
    }
    PrintBCard((int *)bingo,S);
    if(isRowCompleted(bingo,S) == 1)
    {
        printf("\n\nYou Filled out a row - BINGO!!!");
    }
    else //aka is columncompleted
    {
        printf("\n\nYou filled out a column - BINGO!!!");
    }
}












