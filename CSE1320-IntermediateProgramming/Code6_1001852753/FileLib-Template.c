// FileLib Template

#include <stdio.h>
#include <string.h>
#include "ListLib.h"
#define MAXMAPSIZE 20

FILE* OpenFile(int argc, char* argv[])
{	
	/* declare various variables needed */
	FILE* read; //were gonna do read to read the file into the linked list, doing r is gonna get me confused with the r.
	char filename[100];
	/* if argc is 2, then use argv[1] as the input file name, else print the message seen in sample output */
	if(argc==2)
	{
		strcpy(filename, argv[1]);
	}
	else
	{
		printf("Must be ran with an input file name. \n\n Enter file name at the prompt: ");
		fgets(filename, 19, stdin);
		filename[strlen(filename)-1] = '\0';
	}
	do
	{
		/* open file with "r" mode */
		read=fopen(filename, "r");
		/* if file did not open */
		if(read==NULL)
		{
			printf("Could not open file name %s. \n\n Enter a file name at the prompt", filename);
			/* print message seen in sample output */
			fgets(filename, 19, stdin);
			filename[strlen(filename)-1] = '\0';
			/* read in new filename */
			read=fopen(filename, "r");
			/* open the file "r" mode */
		}
	}
	while (read == NULL);
	
	return read;//To go back to read 	
	/* return the file handle */
}

void ReadFileIntoLinkedList(FILE *DCFile, NODE **LinkedListHead)
{
	/* declare various variables needed */
	char buffer[MAXMAPSIZE];
	char *token1 = NULL;
	char *token2 = NULL;
	char tok1;
	char drawcommand[10];

	/* while fgets() reads the file */
	while(fgets(buffer,sizeof(buffer),DCFile))
	{
		/* if line from file ends with \n, then replace \n with \0 */
		if(buffer[strlen(buffer)-1]=='\n')
		{
			buffer[strlen(buffer)-1]='\0';
		}
		/* tokenize to get the Letter and the DrawCommand */
		token1 = strtok(buffer,"|");
		tok1 = *token1;
		token2 = strtok(NULL,"|");
		strcpy(drawcommand, token2);
		
		/* Call AddDrawCommandToList with correct parameters */
		AddDrawCommandToList(tok1, drawcommand,LinkedListHead);
	}
}
