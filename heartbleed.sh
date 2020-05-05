#!/bin/bash

while read line
do
echo "$line"
nmap -p 443 --script ssl-heartbleed $line >> output.txt
done < url.txt
cat output.txt | grep "vulnerable"

