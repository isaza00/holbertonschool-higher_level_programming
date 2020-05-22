#!/bin/bash
cat list | while read line; do echo "if __name__ == \"__main__\":" >> $line; done;
cat list | while read line; do echo -e "\timport doctest" >> $line; done;
cat list | while read line; do echo -e "\tdoctest.testfile(\"example.txt\")" >> $line; done;
