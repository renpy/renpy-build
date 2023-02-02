#!/bin/bash

# Check if the 80 port is occupied
if netstat -an | grep -q ":80 "; then
  echo "Port 80 is occupied, using port 3000 instead"
  port=3000
else
  echo "Port 80 is available"
  port=80
fi

# Check if Python 2 or 3 is installed
if command -v python2 > /dev/null 2>&1; then
  echo "Python 2 is installed"
  python2 -m SimpleHTTPServer $port &
elif command -v python3 > /dev/null 2>&1; then
  echo "Python 3 is installed"
  python3 -m http.server $port &
else
  echo "Python not found"
  exit 1
fi

# Open the browser
xdg-open "http://localhost:$port"