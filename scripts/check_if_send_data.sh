#!/bin/bash

ping -c 1 -q google.com >&/dev/null; echo $?

if [ $? -eq 0 ]; then
    printf "\nonline\n" 
    python sen_files_metadata.py
    python pitaya.py
else
    printf "\noffline\n" 
fi

