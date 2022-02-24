#!/usr/bin/env python3
import sys
import os
# sys.argv: Lista de argumento passado a linha de comando
arguments = sys.argv
num_arguments = len(arguments)

if num_arguments <= 1:
    print('[Error] Missing arguments')
    print('-a', 'List all files', sep='\t')
    print('-d', 'List all directories', sep='\t')

print_files = False
print_dirs = False
if '-a' in arguments:
    print_files = True

if '-d' in arguments:
    print_dirs = True

for file in os.listdir('.'):
    if print_files:
        if os.path.isfile(file):
            print(file)
    if print_dirs:
        if os.path.isdir(file):
            print(file)
