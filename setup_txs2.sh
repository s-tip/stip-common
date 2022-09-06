#!/bin/sh
INSTALL_DIR=/opt/s-tip
COMMON_DIR=/home/stip/stip-common
SCRIPTS_DIR=$COMMON_DIR/install_scripts

## git clone
git clone https://github.com/s-tip/stip-txs2.git
chown -R stip:stip stip-txs2

## apt install
apt install -y python3-dev
apt install -y libpq-dev

## pip install
pip3 install -r $SCRIPTS_DIR/requirements_txs2.txt

# copy TXS2 setting
mkdir -p $INSTALL_DIR/txs2
mkdir -p $INSTALL_DIR/txs2/conf
cp -pr $COMMON_DIR/stip-txs2/bin $INSTALL_DIR/txs2
cp -p $COMMON_DIR/stip-txs2/conf/* $INSTALL_DIR/txs2/conf/
ln -s $COMMON_DIR/stip-txs2/src $INSTALL_DIR/txs2/src
ln -s $INSTALL_DIR/.env $INSTALL_DIR/txs2/.env
ln -s $COMMON_DIR/stip-txs2/version $INSTALL_DIR/txs2/version
mkdir $INSTALL_DIR/txs2/staticfiles
chown -R stip:stip $INSTALL_DIR/txs2

# for Apache2
cp -p $SCRIPTS_DIR/apache/stip-txs2-ssl.conf /etc/apache2/sites-available
cp -p $SCRIPTS_DIR/apache/stip-txs2-console-ssl.conf /etc/apache2/sites-available
a2ensite stip-txs2-ssl
a2ensite stip-txs2-console-ssl

