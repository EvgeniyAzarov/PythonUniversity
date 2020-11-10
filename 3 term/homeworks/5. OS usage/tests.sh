#!/bin/bash

#Clear program cache without output
rm cache/* > /dev/null 2>&1

#Create test environment
rm -rf testdir
mkdir testdir
cd testdir

mkdir dir1
mkdir dir1/dir2
mkdir somedir
mkdir somedir1

echo "some text" > testfile.txt
echo "print("python program")" > dir1/dir2/hello.py
echo "Test" > dir1/file.txt

cd ..

#Run program for the first time
python t22_08.py testdir

#Change test data
cd testdir
echo "test" > dir1/file.txt
rm -rf dir1/dir2
echo "text" > new_file.txt
echo "some new text" > testfile.txt
echo "text1" > somedir/new_file.txt
cd ..

#Run program for the second time
python t22_08.py testdir
