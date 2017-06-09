## the below script will create an env
## that can run some basic neural network
## codes. If you just want the env, stop 
## on row 20.

#!/bin/bash

# install the required packages
sudo apt-get python-pip -y
sudo pip install virtualenv

# check version 
virtualenv --version

# create the environment
mkdir example_env
virtualenv -p /usr/bin/python2.7 example_env/

# start the environment
source autonomio_dev/bin/activate

# install the required python packages
pip install keras 
pip install tensorflow

# install jupyter notebook and start it
pip install jupyter 
jupyter notebook
