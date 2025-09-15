//Name: Mary-Rose Tracy
//ID#:1001852753

#include <stdio.h>
//Realized some of my problems came from not having a stdlib.h
#include <stdlib.h>
//define the bits
#define BITS 8
//need a pointer for binary
void ConvertDecimalToBinary(int num, int *binary) 
{
    // int binary[BITS];
    int k;
    for (int b=BITS-1; b>=0; b--) 
    {
        k = num >> b;
        if (k & 1)
            binary[b] = 1;
        else
            binary[b] = 0;
    }
}

void printBinary(int *bin) 
{
    for (int i=BITS-1; i>=0; i--) 
    {
        printf("%d", bin[i]);
    }
    printf("\n");
}

int main()
{
    int num1, num2;
    char bitwise_op[2];
    int result;
    // for storing the converted Binary value
    int bin1[BITS], bin2[BITS], binResult[BITS];
    //Time for the paragraph of comments for printf. 
    printf("Bitwise Calculator\n\n");
    printf("Enter two base 10 values with a bitwise operator to see the decimal result and the binary result. The format is\n\n");
    printf("First number BitwiseOperator SecondNumber\n\n");
    printf("For example, enter the expression\n\n2 & 3\n\n");
    printf("This calculator can be used with &, |, ^, << and >>\n\n");
    printf("Please note that the spaces between numbers and operator is essential and the two entered values must be between 0 and 255\n\n");
    printf("Enter expression ");
    scanf("%d %s %d", &num1, bitwise_op, &num2);

    ConvertDecimalToBinary(num1, bin1);
    ConvertDecimalToBinary(num2, bin2);
    //need an if else statment for operations & there are five of them so put it in:
    if(bitwise_op[0] == '&') 
    {
        result = num1 & num2;
    } 
    else if (bitwise_op[0] == '|') 
    {
        result = num1 | num2;
    }
    else if (bitwise_op[0] == '<') 
    {
        result = num1 << num2;
    } 
    else if (bitwise_op[0] == '>') 
    {
        result = num1 >> num2;
    } 
    else if (bitwise_op[0] == '^') 
    {
        result = num1 ^ num2;
    } 
    else 
    {
        printf("\nOperator %s is not supported by the calculator.", bitwise_op);
        return 0;
    }
    //convert to binary the result in base 10 part
    ConvertDecimalToBinary(result, binResult);

    printf("In base 10...\n");
    printf("%d %s %d = %d\n\n", num1, bitwise_op, num2, result);//two spaces it looks like

    printf("In 8-bit base 2...\n");
    printBinary(bin1);
    printf("%s\n", bitwise_op);
    printBinary(bin2);
    printf("========\n");
    printBinary(binResult);

    return 0; //finally the end Whew!
}