#!/bin/bash


cat &
1 <<< "what"
sleep 10
#exec gdb < $4
# (gdb $@ <<< "add-auto-load-safe-path "$(pwd)"/python\n") <$0
