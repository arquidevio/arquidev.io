#!/bin/bash

echo "Content-Type: text/html"
echo ""

firstString=$(cat ../index.htm)
inject='<script type="text/javascript">fetch("/cgi-bin/reload.sh").then(() => location.reload());</script>'

echo -e "${firstString/<\/title>/"</title>\n    $inject"}" 
