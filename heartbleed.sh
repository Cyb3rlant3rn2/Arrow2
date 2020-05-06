#!/bin/bash

echo "[+]Vulnerable Domains"
while read line
do

nmap -p 443 --script ssl-heartbleed $line >> output.txt
nmap -p 443 --script ssl-heartbleed $line > tmp.txt
if [ $(cat tmp.txt | grep -o "vulnerable") -e "vulnerable" ]
then
echo "$line"
fi
done < url.txt

