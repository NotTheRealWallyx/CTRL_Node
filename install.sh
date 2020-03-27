#!/bin/bash

correct_python_message(){
    echo "true";
    echo "[OK] -- Python 3 installed"
}

create_virtual_env(){
    python3 setup.py install
}

not_version_error(){
    echo "You need Python 3 for this application to work";
    echo "Check the FAQ Section in the README for more info.";
    echo " - - - - - - - - - - - - - - - - - - - - - - - -";
    echo "Thanks, bye :)";
}
export_python(){
    PROJECT_ROOT_ABSOLUTE_PATH=$(pwd)
    export PYTHONPATH="$PROJECT_ROOT_ABSOLUTE_PATH:$PYTHONPATH"
}

echo "Making Initial checks:"

# Check if Python 3 is installed
if [[ "$(python3 -V)" =~ "Python 3" ]]; then
    create_virtual_env
    export_python
else
    not_version_error
fi