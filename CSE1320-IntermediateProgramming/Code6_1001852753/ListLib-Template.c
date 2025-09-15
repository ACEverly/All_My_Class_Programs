
#include <stdio.h>
#include <string.h>

#include "ListLib.h"
void AddDrawCommandToList(char letter, char drawcommand[10], NODE **LinkedListHead)
{
    NODE *TempPtr, *NewNode; //tempPtr = tempointer
	/* declare pointers of type NODE named TempPtr and NewNode */
    NewNode = malloc(sizeof(NODE));
	NewNode->Letter=letter;

	NewNode->DrawCommand=malloc(strlen(drawcommand));
	strcpy(NewNode->DrawCommand,drawcommand);

	NewNode->next_ptr=NULL;
	/* malloc a new node and assign the Letter and the DrawCommand (after mallocing memory for it) */

	/* If the LinkedListHead is NULL, then give it the address of the new node */
	/* Else traverse to the end of the linked list and add the new node */
	if(*LinkedListHead==NULL)
	{
		*LinkedListHead = NewNode;
	}
	else
	{
		TempPtr=*LinkedListHead;
		while(TempPtr->next_ptr!=NULL)
		{
			TempPtr=TempPtr->next_ptr;
		}
		TempPtr->next_ptr=NewNode;
	}
}

NODE* FindLetter(NODE *LinkedListHead, char letter, char DC[])
{
	/* while traversing the linked list AND the Letter in the node is not the Letter passed in */
	NODE *TempPtr;
	TempPtr=LinkedListHead;
	while(TempPtr!=NULL && TempPtr->Letter!=letter)
	{
		TempPtr=TempPtr->next_ptr;
		/* move TempPtr */
	}

	if (TempPtr!=NULL)
	{
		strcpy(DC,TempPtr->DrawCommand);
		/* copy the DrawCommand from the node into the passed in parameter */
		/* return the next pointer stored in TempPtr */
		return TempPtr->next_ptr;
	}
	return TempPtr;
	/* return TempPtr */
}
