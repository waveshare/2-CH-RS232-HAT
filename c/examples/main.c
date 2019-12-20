#include <stdio.h>      //printf()
#include <stdlib.h>     //exit()
#include <signal.h>
 #include <stdio.h>
#include "DEV_Config.h"

void  Handler(int signo)
{
    //System Exit
    printf("\r\nHandler:Program stop\r\n"); 

    DEV_ModuleExit();

    exit(0);
}

int main(int argc, char **argv)
{
    // Exception handling:ctrl + c
    signal(SIGINT, Handler);
    
    if (DEV_ModuleInit()==1)return 1;
    
    DEV_UART_Init("/dev/ttySC0");
    
    UBYTE pData[100]={0};
    int i=0;
    
    UART_Write_nByte("Waveshare 2-CH RS232 HAT\r\n", 26);
    while(1){
        pData[0] = UART_Read_Byte();
        printf("%c",pData[0]);
        UART_Write_nByte(pData, 1);
    }
    DEV_ModuleExit();
    return 0; 
}
