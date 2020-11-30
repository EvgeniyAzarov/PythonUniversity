#!/bin/bash

rm -rf pr2_test/path*
cp -r pr2_test_template/path1 pr2_test/path1
cp -r pr2_test_template/path2 pr2_test/path2

python pmodc2w2_pr2.py pr2_test/path1 pr2_test/path2
