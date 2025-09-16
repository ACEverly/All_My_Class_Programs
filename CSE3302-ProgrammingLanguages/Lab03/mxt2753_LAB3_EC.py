#mxt2753_LAB3_EC.py
#Name: Mary-Rose Tracy
#ID#: 1001852753
#Date: 10/18/2023
#Os VS Code Microsoft used
import os #you should only need to use the ‘os’ package, if you want to use any other package you must get permission beforehand.
#"If you want to attempt extra credit, you will turn in two(2) files.  Do not put the extra credit code in the same file as the regular assignment. 
# You may use a copy of your own Lab03 code and extend it for extra credit, as long as it is in a separate file.
#Write a separate program that can input an algebraic expression and convert it to RPN and 
#then evaluate the RPN. Print the RPN and the result in separate lines. 
#If you are implementing extra credit, your file should be name as <netid>_Lab03_EC.py. 
#The input file name will be input_RPN_EC.txt and it will have algebraic expressions.
#Add at least one more operator (unary subtraction, or modulo division, etc.). 
#You must document what operators you are adding.
#Add which ones to comments and make sure to include that as well in your submission so the GTA knows to test using the extra scenarios.""
def IToPNot(Formu): #Fix: in->post Fix: In -> post (NOTation)
    #NEWWWWW  VVVVVV
    #lets get the Solut
    Solut=[ ] #need to get the operators then make then have prorit
    PEMDAS={ "+":1,"-":1,"*":2,"/":2,"%":2 } 
    #NEWWWWW   ^^^^^
    #Old Code: PileStck
    #let's start the PileStk
    PileStk=[ ] 
    for TOK in Formu:
        #Go through and repeat Formu
        if TOK.isdigit( ): 
            Solut.append( TOK )
        #kept on messing up due to the ()
        elif TOK=="(":
            PileStk.append( TOK )
        elif TOK==")":
            while PileStk and PileStk[ -1 ]!="(":
                Solut.append( PileStk.pop( ) )
            PileStk.pop( )
        else:
            while PileStk and PEMDAS.get( TOK,0 )<=PEMDAS.get( PileStk[ -1 ], 0 ):
                Solut.append( PileStk.pop( ) )
            PileStk.append( TOK )
    while PileStk: #finnish the outcome by popping the OP. make them append
        Solut.append( PileStk.pop( ) )
    #now return the Solut aka The calc Formu
    return Solut
#Same code from last time: 
#"Use Python to create a simple calculator that accepts Reverse Polish Notation" 
#"(RPN) and displays the final answer (Intermediate steps or results need not be displayed)."
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
            #"It only accepts 4 operators “+”, “-“, “*”, “/”. so let's do it in order
            #we also need to push it.
            if TOK=="+":
                PileStk.append( OperOne+OperTwo )
            elif TOK=="-":
                PileStk.append( OperOne-OperTwo )
            elif TOK=="*":
                PileStk.append( OperOne*OperTwo )
            elif TOK=="/":
                PileStk.append( OperOne/OperTwo )
            elif TOK=="%": 
                PileStk.append( OperOne%OperTwo )
    return PileStk[ 0 ] #The end willbe 1 element out it
#Now for the main
#Since we are not suppose to do anything with the Solut. AKA the user doesn't input.
#instead we are suppose to do make the program go get the input_RPN
def main( ):
    with open( os.path.join( os.getcwd( ),"input_RPN_EC.txt" ) ,"r" ) as DataFile: #r meaning read
        for Source in DataFile:
            #Formu=Source.strip( ).split( ) //let's put them in metaphorical boxes. Then solve and solve it
            #print( CalcRPN ( expression ) )
            StartFormu=Source.strip( ).split( ) #let's put them in metaphorical boxes. Then solve and solve it
            TailFormu=IToPNot( StartFormu )
            print( "Formula:", " ".join ( TailFormu ) )
            print( "Outcome:", CalcRPN ( TailFormu ) )
            #print out Formu with calc result
#print(result)
if __name__=="__main__":
    main()
#couldnt figure out why I kept getting errors on this one^