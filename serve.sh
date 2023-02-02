#!/bin/bash

PORT=8090
fuser -k $PORT/tcp
busybox httpd -p $PORT -c httpd.conf && \
echo "Listening on http://localhost:$PORT"
echo "Use: fuser -k $PORT/tcp to exit"
