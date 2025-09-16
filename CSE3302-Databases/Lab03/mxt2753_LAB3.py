#mxt2753_LAB3.py
#Name:Mary-Rose Tracy
#ID#:1001852753
#Date:10/18/2023
#Os VS Code Microsoft used
#"Use Python to create a simple calculator that accepts Reverse Polish Notation" 
#"(RPN) and displays the final answer (Intermediate steps or results need not be displayed)."
import os #you should only need to use the ‘os’ package, if you want to use any other package you must get permission beforehand.
def CalcRPN( Formu ):
    #let's start the PileStk
    PileStk=[ ] 
    #let's do a for and define it
    for TOK in Formu:
        #If= TOK = anum= push
        if TOK.isdigit( ):
            PileStk.append( int ( TOK ) )
        #We defined what a TOK =, and finnish by popping now we gonna define what is the operators
        else:
            #Operand 1 & 2
            OperTwo=PileStk.pop(  )
            #Tried OperOne then Two didn't know why I was getting negative numbers
            OperOne=PileStk.pop(  )
            #"It only accepts 4 operators “+”, “-“, “*”, “/”. So lets do it in order
            #we also need to push it.
            if TOK=="+":
                PileStk.append( OperOne+OperTwo )
            elif TOK=="-":
                PileStk.append( OperOne-OperTwo )
            elif TOK=="*":
                PileStk.append( OperOne*OperTwo )
            elif TOK=="/":
                PileStk.append( OperOne/OperTwo )
    return PileStk[ 0 ] #The end willbe 1 element out it
#Now for the main
#Since we are not suppose to do anything with the output. AKA the user doesn't input.
#instead we are suppose to do make the program go get the input_RPN
def main( ):
    with open( os.path.join( os.getcwd( ),"input_RPN.txt" ) ,"r" ) as DataFile: #r meaning read
        for Source in DataFile:
            Formu=Source.strip( ).split( ) #let's put them in metaphorical boxes. Then solve it
            print(CalcRPN ( Formu ) )
#print(result)
if __name__=="__main__":
    main( )
#couldnt figure out why I kept getting errors on this one^