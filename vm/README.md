Files in this folder
 - **./benchmarks**: Contains files from our benchmark result with 
     different memory amount stressed. l denote result is from our
     changed code, n denote the normal QEMU implementation.
 - **./mount**: Expected to be mount point for shared lubuntu.img
     for live migration.
 - **./command**: Contain the migration command to be ran on QEMU 
     virtual guest console. Requires modification to IP address 
     to address of waiting VM to work. Might be 127.0.0.1 for 
     localhost.
 - **./mount.example.sh**: Is the example mount script. Change IP
     address for ssh mount.
 - **./start-wait.sh**: Starts QEMU waiting for live migration.
 - **./start.sh**: Starts QEMU with lubuntu image with 512MB of ram.
 - **./stress.sh**: To be copied into VM and runned to stress the 
     VM. Change the memory amount to change the amount of pages 
     to dirty.
 - **./unmount.sh**: Unmount the shared drive from ./mount.
 
