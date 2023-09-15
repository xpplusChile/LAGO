#!/bin/bash

ping -c 1 -q google.com >&/dev/null; echo $?

if [ $? -eq 0 ]; then
    printf "\nonline\n" 
    python sen_files_metadata.py #log con peso y cantidad de archivos mandados
    python pitaya.py             #manda los archivos y los borra los mandados de la memoria interna
else
    printf "\noffline\n" 
fi

