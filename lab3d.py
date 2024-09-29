#!/usr/bin/env python3
# Author ID: hrai9

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = p.communicate() # captures the stdout and stderr
    stdout = output.decode('utf-8').strip() # decode bytes to string
    return stdout

if __name__ == "__main__":
    print(free_space())