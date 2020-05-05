#!/usr/bin/bash
echo "Printing 200 ok list"
echo "====================="
cat output.txt | grep 200
echo ""
echo ""
echo "Printing 404 list"
echo "====================="
cat output.txt | grep 404
echo ""
echo ""
echo "Printing 302 list"
echo "====================="
cat output.txt | grep 302
echo ""
echo ""
