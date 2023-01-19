#!/bin/sh

watch -d -t -g -n 1 "ls -lR --full-time ../ | sha1sum"

echo "Content-Type: text/html"
echo ""
echo "OK"