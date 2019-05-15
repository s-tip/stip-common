#!/bin/sh
VERSION="v0.1.0"
INSTALL_DIR=/opt/s-tip
COMMON_DIR=/home/stip/stip-common
SCRIPTS_DIR=$COMMON_DIR/install_scripts

# git clone
git clone https://github.com/s-tip/stip-txs.git
chown -R stip:stip stip-txs

## apt install
apt install -y supervisor gunicorn

## pip install
pip install libtaxii
pip install opentaxii==0.1.7

# copy TXS setting
mkdir -p $INSTALL_DIR/txs
cp -pr $COMMON_DIR/stip-txs/conf $INSTALL_DIR/txs
cp -p $COMMON_DIR/stip-txs/init.d/supervisord.conf /etc/supervisor/
cp -p $COMMON_DIR/stip-txs/init.d/conf.d/stip-taxii-server.conf /etc/supervisor/conf.d/
cp -pr $COMMON_DIR/stip-txs/init.d/conf.d/cert /etc/supervisor/conf.d/
ln -s $COMMON_DIR/stip-txs/src $INSTALL_DIR/txs/src
echo $VERSION > $INSTALL_DIR/txs/version
chown -R stip:stip $INSTALL_DIR/txs