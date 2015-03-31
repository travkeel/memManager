#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

#define MAXPROC 10

void execute()
{
    pid_t pid;
    int status;

    if ((pid = fork()) < 0) { //Fork a child process
       fprintf(stderr, "*** ERROR: forking child process failed\n"); 
    }
    else if (pid == 0) { //Child process
     //Execute child process here
    }
    else {  //Parent process
        while(wait(&status) != pid)
            ;
    }
}


int main()
{
    char line[1024];
    char *argv[64];

    while(1)
    {
        fputs("sysadmin@bleh: ", stdout); //prompt for the user
        fgets(line, sizeof(line-1), stdin); //line to be read in
        execute();
    }    
}
