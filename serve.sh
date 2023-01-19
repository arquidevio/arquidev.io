#!/bin/bash

PORT=8090
busybox httpd -p $PORT && \
echo "Listening on http://localhost:$PORT" && \
echo "Use: fuser -k $PORT/tcp to exit"
