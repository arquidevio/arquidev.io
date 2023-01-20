#!/bin/bash

PORT=8090
fuser -k $PORT/tcp
busybox httpd -p $PORT && \
echo "Listening on http://localhost:$PORT"
echo "Use: fuser -k $PORT/tcp to exit"
