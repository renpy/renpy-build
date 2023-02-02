@echo off

rem Check if the 80 port is occupied
netstat -an | find ":80 " > nul
if %ERRORLEVEL% == 0 (
  echo Port 80 is occupied, using port 3000 instead
  set port=3000
) else (
  echo Port 80 is available
  set port=80
)

rem Check if Python 2 or 3 is installed
python -V 2>&1 | find "Python 2" > nul
if %ERRORLEVEL% == 0 (
  echo Python 2 is installed
  start "" "cmd /c python -m SimpleHTTPServer %port%"
) else (
  echo Python 3 is installed
  start "" "cmd /c python -m http.server %port%"
)

rem Open the browser
start "" "http://localhost:%port%"