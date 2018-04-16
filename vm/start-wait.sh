#!/bin/bash

sudo /usr/local/bin/qemu-system-x86_64 -hda mount/lubuntu.img -boot c -m 512M -incoming tcp:0:4444
