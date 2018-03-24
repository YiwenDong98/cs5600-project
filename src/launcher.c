#include <unistd.h>
#include <stdlib.h>
#include <string.h>

/**
 * First argument is the string to pass to stdin of program.
 * Second argument is the program to execute
 * Rest of the arguments are passed on to the program as normal arguments
 */
int main(int argc, char *argc[]) {
    int stdin = 0;
    int stdout = 1;
    int stderr = 2;
    pid_t fork();
    if (pid_t == 0) {
        int err = execv(argc[2], argc + 3);
        exit(err);
    }
    write(stdout, argc[1], strlen(argc[1]));
    wait(pid_t);
}
