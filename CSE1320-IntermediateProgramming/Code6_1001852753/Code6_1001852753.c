//Mary-Rose Tracy 
//ID#:1001852753

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "DrawTool.h"
#include "ListLib.h"
#include "FileLib.h"

void FreeVars(NODE **LinkedListHead); //were gonna use this 
void FreeVars(NODE **LinkedListHead)
{
    NODE *NEXT, *CURRENT; //need a pointer to node and current
    NEXT=*LinkedListHead;
    while(NEXT != NULL)
    {
        CURRENT=NEXT;
        NEXT=NEXT->next_ptr;
        free(CURRENT->DrawCommand);
        free(CURRENT);
    }
}

int main(int argc, char *argv[])
{
    FILE *read=OpenFile(argc,argv); //need to open the file 

    NODE *LinkedListHead = NULL;

    char userinput[4];
    //char drawcommand[10]={0};

    ReadFileIntoLinkedList(read,&LinkedListHead);
    fclose(read);
    char mymap[MAXMAPSIZE][MAXMAPSIZE];
    InitializeMap(mymap);
    printf("Please enter 1-3 letter: ");
    scanf(" %s",userinput);
    while(strlen(userinput)<1 || strlen(userinput)>3)
    {
        printf("You didn't enter 1-3 letters. Please try again: ");
        scanf(" %s", userinput);
    }
    char *linptr='\0';
    char linstr[4]={0};
    char *iptr='\0'; //ipointer 
    char *jptr='\0'; //jpointer
    char *kptr='\0'; //kpointer  
    int x=0; //set x,y,and z 
    int y=0;
    int z=0;
    
    char *drawsymbptr='\0';
    char drawsymb[4]={0};

    NODE *TempPtr = LinkedListHead;
    for (int i=0 ; i<strlen(userinput); i++)//make a for loop and  stringlength the user input
    {
        userinput[i]=toupper(userinput[i]);
        while (TempPtr!=NULL)
        {
            char DC[10]={0};
            TempPtr=FindLetter(TempPtr,userinput[i],DC);
            
            if(DC[0]!= '\0')
            {
                linptr=strtok(DC,"(),"); //gathering a token akak strtok it and make a strcopy of it
                strcpy(linstr, linptr);
                linstr[0]=toupper(linstr[0]);
                iptr=strtok(NULL,"(),");
                x=atoi(iptr);
                jptr=strtok(NULL,"(),");
                y=atoi(jptr);
                kptr=strtok(NULL,"(),");
                z=atoi(kptr);
                drawsymbptr=strtok(NULL,"(),");
                strcpy(drawsymb,drawsymbptr);
                if(drawsymb[0]=='\n')
                {
                    drawsymb[0]='X';
                }
                if(linstr[0]=='P')
                {
                    if(i==0)
                    {
                        mymap[x][y]=drawsymb[0];
                    }
                    else if(i==1)
                    {
                        mymap[x][y+7]=drawsymb[0];
                    }
                    else
                    {
                        mymap[x][y+14]=drawsymb[0];
                    }
                }
                else if(linstr[0]=='V')
                {
                     if (i==0)
                    {
                        DrawLine(mymap,x,y,linstr[0],z,drawsymb[0]);
                    }
                    else if (i==1)
                    {
                        DrawLine(mymap,x,y+7,linstr[0],z,drawsymb[0]);
                    }
                    else
                    {
                        DrawLine(mymap,x,y+14,linstr[0],z,drawsymb[0]);
                    }
                }
                else if(linstr[0]=='H')
                {
                    if (i==0)
                    {
                        DrawLine(mymap,x,y,linstr[0],z,drawsymb[0]);
                    }
                    else if (i==1)
                    {
                        DrawLine(mymap,x,y+7,linstr[0],z,drawsymb[0]);
                    }
                    else
                    {
                        DrawLine(mymap,x,y+14,linstr[0],z,drawsymb[0]);
                    }
                }
            }
        }
        TempPtr=LinkedListHead;
        
    }
    PrintMap(mymap);
    FreeVars(&LinkedListHead);


    return 0;
}
