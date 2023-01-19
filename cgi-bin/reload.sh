#!/bin/sh

watch -d -t -g "ls -lR --full-time ../ | sha1sum"

echo "Content-Type: text/html"
echo ""
echo "OK"