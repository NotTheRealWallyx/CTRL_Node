#!/bin/bash

correct_python_message(){
    echo "true";
    echo "[OK] -- Python 3 installed"
}

install_with_poetry(){
    poetry install
}

not_version_error(){
    echo "You need Python 3 for this application to work";
    echo "Check the FAQ Section in the README for more info.";
    echo " - - - - - - - - - - - - - - - - - - - - - - - -";
    echo "Thanks, bye :)";
}

echo "Making Initial checks:"

# Check if Python 3 is installed
if [[ "$(python3 -V)" =~ "Python 3" ]]; then
    correct_python_message
    install_with_poetry
    echo "[OK] -- Run the app with: poetry run ctrl-node"
else
    not_version_error
fi
