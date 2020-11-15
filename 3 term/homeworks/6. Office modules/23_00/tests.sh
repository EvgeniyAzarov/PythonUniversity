#!/bin/bash
cp -r input_template/ input/
python t23_08.py -f "\b\w{2}x\w\b" -r "math" input
