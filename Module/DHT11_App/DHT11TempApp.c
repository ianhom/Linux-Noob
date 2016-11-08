#define _GNU_SOURCE
#include <string.h>
#include <unistd.h> 
#include <stdlib.h> 
#include <sys/types.h> 
#include <sys/stat.h> 
#include <sys/ioctl.h> 
#include <fcntl.h>
#include <linux/fs.h> 
#include <errno.h> 
#include <stdarg.h>
#include <stdio.h>
#include <pthread.h>


int main()
{
    int ret = -1;
    char buff[255];
    memset(buff, 0, sizeof(buff));

    FILE *fp = fopen("/sys/devices/platform/dht11/iio:device0/in_temp_input","r");
    if(NULL == fp)
    {
        printf("Can not open/sys/devices/platform/dht11/iio:device0/in_temp_input\n");
        return -1;
    }
    else
    {
        if(fread(buff, sizeof(char), sizeof(buff)-1,fp) >0)
        {
            printf("Reading is success!!\n");
            printf("The Temperature value is %d\n", atoi(buff));
            ret = 0;
        }
    }
    fclose(fp);

    return 0;
}
