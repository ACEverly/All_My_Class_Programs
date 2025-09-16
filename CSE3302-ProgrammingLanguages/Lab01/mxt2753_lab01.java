/*
Name: Mary-Rose Tracy
ID#:1001852753
Using Windows, using VS Code
In Language of: java
*/
//Let's plug in the Imports
import java.io.File;
//Let's just put it all in one function for the Directory Space
public class mxt2753_lab01 
{
    //Now let's calc sixe of filles = all in a file direct
    public static int DirSpace(File DR)
    {
        int Sum=0;
        //Literally in the psudocode
        File[] MultOEntry=DR.listFiles(); //We need to list all the stuff
        for(File entry:MultOEntry) //redo the entries NOTE: this part is kind of like C
        {
            if(entry.isFile()) //Computer reads if entry ='s the file + size to the overall amount.
            {
                Sum+=entry.length();
            }
            else if(entry.isDirectory()) //If entry=directory, recursive calc to get the overall amount for size.
            {
                Sum+=DirSpace(entry);
            }
        }
        return Sum; //From psyudeocode
    }
    public static void main(String[] args) //Time ofr the main which is the easiest part
    {
        String TargetDir="."; // Dir starts counting amount of size.
        int Sum=DirSpace(new File(TargetDir)); //Calc amound of size with the start of the target.
        System.out.println(Sum); //Print amount of size.
    }
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
