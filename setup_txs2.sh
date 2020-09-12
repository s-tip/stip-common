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

# copy TXS21 setting
mkdir -p $INSTALL_DIR/txs21
cp -pr $COMMON_DIR/stip-txs2/bin $INSTALL_DIR/txs21
ln -s $COMMON_DIR/stip-txs2/src $INSTALL_DIR/txs21/src
cp -pr $SCRIPTS_DIR/env_txs21 $INSTALL_DIR/txs21/.env
ln -s $COMMON_DIR/stip-txs2/version $INSTALL_DIR/txs21/version
mkdir $INSTALL_DIR/txs21/staticfiles
chown -R stip:stip $INSTALL_DIR/txs21

# for Apache2
cp -p $SCRIPTS_DIR/apache/stip-txs21-ssl.conf /etc/apache2/sites-available
cp -p $SCRIPTS_DIR/apache/stip-txs21-console-ssl.conf /etc/apache2/sites-available
a2ensite stip-txs21-ssl
a2ensite stip-txs21-console-ssl

