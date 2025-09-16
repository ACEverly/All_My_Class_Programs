
/*
Name: Mary-Rose Tracy
ID#:1001852753
Using Windows, using VS Code
In Language of: C
*/
//Let's do the basic includes
#include <stdio.h>
#include <string.h>
#include <unistd.h>
//The special ones from the library you said we can use: These ones seem to be ones that look quite useful
#include <sys/stat.h>
#include <dirent.h>
#include <sys/types.h>


//We need that recursive funct
int DirSpace(const char *DR);

int DirSpace(const char *DR) 
{
    //Our declarations
    //int & Strings
    int Sum=0;
    char PWay[1024];
    //The Structs
    struct stat SubStat;
    struct dirent *entry; // entry variable From psyduocode
    //Wondered why it didnt work Needed DIR
    DIR *TheDDir;
    if(!(TheDDir=opendir(DR))) //Let's make it open the directory
        return 0;
    while((entry=readdir(TheDDir))!=NULL)//Now traverse entries for the direct
    {
        if(strcmp(entry->d_name,".")==0||strcmp(entry->d_name,"..")==0) //We need to jump from parents of direct
            continue;
        snprintf(PWay,sizeof(PWay),"%s/%s",DR,entry->d_name); //Let's make a Build a way for the present enter
        if(stat(PWay,&SubStat)==-1) //Tell the computer to give us the stats of it
            continue;
        if(S_ISDIR(SubStat.st_mode)) // Reads If there's direct, calculate the amount via size with recuurse
            Sum+=DirSpace(PWay);
        // FORGOT this part If there's a file, add to the Sum w/ direct
        else
            Sum+=SubStat.st_size;
    }
    closedir(TheDDir); //Now we need to close it AKA closedir
    return Sum;
}
int main()
{
    const char *TargetDir="."; //From Psyudeocode
    int AmountOSize=DirSpace(TargetDir); 
    printf("%d\n",AmountOSize);
    return 0;
}

/*
Pseudocode Given In class:
Lab 1: DirSpace
TargetDir =”.”
int Sum=0;
Sum = Dirspace(TargetDir)
Print sum;
—------ 
int DirSpace(Str Dir)
int sum=0;
For each entry in Dir // siCip ‘.’ + ‘..’
If entry is file 
 Sum +=size(file)
if entry is Dir sum+=DirSpace(entry)
Return sum
*/