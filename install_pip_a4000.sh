#!/usr/bin/env bash



echo "Installing python3.10"
sudo apt install python3.10 python3.10-dev python3.10-venv -y

echo "Creating virtual environment"
python3.10 -m venv deca-env
echo "Activating virtual environment"

source $PWD/deca-env/bin/activate
$PWD/deca-env/bin/pip install -r requirement_a4000.txt