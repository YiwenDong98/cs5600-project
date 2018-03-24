#Make file for the launcher
CC=gcc
CFLAGS=-g -O0 -std=gnu11 -fPIC -Werror -Wno-error=unused-variable -Wall -lpthread -lrt
HEADERS= #Add list of header files

all: clean launcher

clean: 
	rm -rf src/*.o launcher

%.o: %.c ${HEADERS}
	$(CC) $(CFLAGS) $< -c -o $@

launcher: src/launcher.o
	$(CC) $(CFLAGS) $^ -o launcher
