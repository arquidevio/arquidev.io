#!/bin/sh

watch -d -t -g "ls -lR ../ | sha1sum"

echo "Content-Type: text/html"
echo ""
echo "OK"