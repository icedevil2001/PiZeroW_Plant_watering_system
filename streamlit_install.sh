## https://discuss.streamlit.io/t/raspberry-pi-streamlit/2900/26
##

# Download the package repo keyring
wget https://apache.bintray.com/arrow/debian/apache-arrow-archive-keyring-latest-buster.deb

# Install it
sudo apt install ./apache-arrow-archive-keyring-latest-buster.deb

# Update apt
sudo apt update

# Install apache arrow headers
sudo apt install libarrow-dev
sudo apt install libarrow-python-dev

# Install streamlit

PYARROW_CMAKE_OPTIONS="-DARROW_ARMV8_ARCH=armv8-a" pip install streamlit




