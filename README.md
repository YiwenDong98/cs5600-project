# Improve Live Migration(QEMU)

Masters branch contains the modified code while benchmark branch contains 
the origonal QEMU code that our work is based off of. migrate-improve-lmap 
is the working branch for our improvement feature.

QEMU folder contains all the code to build and install QEMU. VM folder 
contaions all the supporting scripts for running live migration and the 
script to run within the VM to benchmark migration performance.

There's videos that walks through cloning repo, building and installing 
QEMU and running benchmarks for live migration from start to finish.

Videos
 - [Demo Custom QEMU Migration](https://youtu.be/e1P9CLL__iY)
 - [Demo Custom QEMU Migration x4](https://youtu.be/17HQJNdDvng)
 - [Demo Default QEMU Migration](https://youtu.be/eg5G4wAcKyk)
 - [Demo Default QEMU Migration x4](https://youtu.be/8nHlbjmhmnU)
 
The Default videos show building from the benchamrk branch which 
contains the unchanged QEMU build and the Custom videos show building from 
our modified code. x4 is the normal video speeded up 4 times. 

The general step is as follows.

 1. Inside QEMU directory, 
    * mkdir build
    * ../configure
    * make -j8
    * sudo make install
 2. Inside VM directory,
    * Modify ./mount.example.sh to mount a shared mount to ./mount that 
        contains lubuntu.img
    * Run modified script to mount a share onto ./mount
    * Run ./start.sh to start the VM
    * Run ./start-wait.sh to start another VM to wait
    * Run ./stress.sh inside the VM to simulate a workload
    * Do control+alt+2 to change to qemu console.
    * Run the command inside ./command on the qemu console to migrate 
        the VM. Change IP address to something like 127.0.0.1 for 
        migrating to a waiting VM on the same machine.
        
*note 1: you can do 'info migrate' within qemu console to find status of 
    migration but will cause significant slowdown to migration progress*
    
*note 2: migration generally takes a minuet, but can take upwards of 5 
    minuets. Super high memory usage from ./stress.sh can cause infinite
    transfer time.*
