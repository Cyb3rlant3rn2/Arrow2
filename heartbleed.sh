#!/bin/bash

while read line
do
echo "[+]Vulnerable Domains
nmap -p 443 --script ssl-heartbleed $line >> output.txt
nmap -p 443 --script ssl-heartbleed $line > tmp.txt
if [ $(cat tmp.txt | grep -o "vulnerable") == "vulnerable"]
then
echo "$line"
fi
done < url.txt


