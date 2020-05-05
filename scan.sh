#!/bin/bash

while read line
do
echo "$line"
nmap -sC -sV  $line >> scan_result.txt
done < url.txt


