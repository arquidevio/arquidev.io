#!/bin/bash

echo "Content-Type: text/html"
echo ""

firstString=$(cat ../index.htm)
inject='
<script type="text/javascript">
  async function WaitForReload() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = () => { 
        if (xmlHttp.readyState == 4) { location.reload(); }
    }
    xmlHttp.open("GET", "/cgi-bin/reload.sh", true);
    xmlHttp.send(null);
  }
  
  WaitForReload();
</script>'

echo -e "${firstString/<\/title>/"</title>\n    $inject"}" 
