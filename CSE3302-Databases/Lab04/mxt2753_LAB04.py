#mxt2753_LAB04.py
#Name:Mary-Rose Tracy
#ID#:1001852753
#Date:11/21/2023
#OS: VS Code Microsoft used, python 3
with open("input.txt","r")as File: #First let's intitialize the input so we can get it done and over with.
    IfBraceIsCompl=0  #We need 3 initialis all intializing from 0.
    SumOBrace=0
    Sum=0
    Statem=False #Let's do what is FALSE STATEMENTS
    StatementIn=False
    StrIn=False 
    for Sent in File: #We need to get every Sent from the file then go thorugh every one of the Sent
        #then arrange it including a loop.
        try:
            for LetNumSym in Sent: #Go through each LetNumSym and see what they are utilizing ifs
                # Check for quotes and update StrIn state
                if LetNumSym=='"': #if the LetNumSym is "" then we need to mess with it.
                    StrIn=not StrIn
                if LetNumSym=='/' and Sent[Sent.find(LetNumSym)+1]=='*'and not StrIn: #We need to analyze and see if it is a block statment, 
                    #if so then it's a not.
                    StatementIn=True
                if StatementIn and LetNumSym=='*' and Sent[Sent.find(LetNumSym)+1]=='/':
                    StatementIn=False
                if LetNumSym=='/' and Sent[Sent.find(LetNumSym)+1]=='/' and not StrIn:
                    Statem=True
                if Statem and LetNumSym=='\n':
                    Statem=False
                if not StrIn and not StatementIn and not Statem: #now if it's a '{}' we need to manipulate in order to have the Sum
                    if LetNumSym=='{':
                        SumOBrace+=1
                    elif LetNumSym=='}':
                        IfBraceIsCompl+=1
            if SumOBrace>0 and IfBraceIsCompl==0: #the f stands for float can space it out or it freaks out.
                Sum=SumOBrace #we need to check the bracket the exterior
            print(f"{Sum} {Sent.rstrip()}") #nwow we print the Sentence
            #matching bracket decreses Sum
            if IfBraceIsCompl>0:
                Sum=SumOBrace-IfBraceIsCompl        
        except Exception as e:
            print(f"Failure of understanding of sentence:{e}") #if the brace is not there, then we have an error. 
    if SumOBrace!=IfBraceIsCompl:
        if Sum>0:
            print("Fail: "+str(Sum)+" No '}' to complete the brackets.")
        elif Sum<0:
            print("Fail: "+ str(-Sum)+" No '{' to complete the beckets.")
            #have a negative Sum aka string then we can't find the {}