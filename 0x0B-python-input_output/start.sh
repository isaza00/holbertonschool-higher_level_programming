#!/bin/bash
cat list | while read line; 
do echo -e "#!/usr/bin/python3\n\"\"\"\n\tModule Comment\n\"\"\"\n\n\n>" > $line;
done;
chmod u+x *.py