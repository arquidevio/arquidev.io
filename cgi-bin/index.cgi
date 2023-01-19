#!/bin/bash

echo "Content-Type: text/html"
echo ""

index=$(cat ../index.htm)
inject='<script type="text/javascript">fetch("/cgi-bin/reload.sh").then(() => location.reload());</script>'

echo -e "${index/<\/title>/"</title>\n    $inject"}" 
