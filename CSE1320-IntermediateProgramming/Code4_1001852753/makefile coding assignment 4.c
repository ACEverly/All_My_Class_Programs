#Mary-Rose Tracy 1001852753 Coding Assignment 4 < input.txt

SRC1 = Code4_1001852753.c
SRC2 = DrawTool.c
SRC3 = ListLib.c 


OBJ1 = $(SRC1:.c=.o)
OBJ2 = $(SRC2:.c=.o)
OBJ3 = $(SRC3:.c=.o)
EXE = $(SRC1:.c=.e)

HFILES = DrawTool.h 
HFILES = ListLib.h 

CFLAGS = -g

all : $(EXE)
 
$(EXE): $(OBJ1)  $(OBJ2)  $(OBJ3)
	gcc $(CFLAGS) $(OBJ1) $(OBJ2) $(OBJ3) -o $(EXE) 

$(OBJ1) : $(SRC1)  $(HFILES)
	gcc -c $(CFLAGS) $(SRC1) -o $(OBJ1)

$(OBJ2) : $(SRC2)  $(HFILES)
	gcc -c $(CFLAGS) $(SRC2) -o $(OBJ2)

$(OBJ3) : $(SRC3)  $(HFILES)
	gcc -c $(CFLAGS) $(SRC3) -o $(OBJ3)