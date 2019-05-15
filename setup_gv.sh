#!/bin/sh
VERSION="v0.1.0"
INSTALL_DIR=/opt/s-tip
COMMON_DIR=/home/stip/stip-common
SCRIPTS_DIR=$COMMON_DIR/install_scripts

## git clone
git clone https://github.com/s-tip/stip-gv.git
chown -R stip:stip stip-gv

## pip install
pip install -r $SCRIPTS_DIR/requirements_gv.txt

## copy GV setting
mkdir -p $INSTALL_DIR/gv/bin
mkdir -p $INSTALL_DIR/gv/conf
mkdir -p $INSTALL_DIR/gv/staticfiles
# for STIX file upload
mkdir -p $INSTALL_DIR/gv/stix
ln -s $COMMON_DIR/stip-gv/src $INSTALL_DIR/gv/src
cp -p $COMMON_DIR/stip-gv/bin/* $INSTALL_DIR/gv/bin/
cp -p $COMMON_DIR/stip-gv/conf/* $INSTALL_DIR/gv/conf
cp -p $SCRIPTS_DIR/env_gv $INSTALL_DIR/gv/.env
echo $VERSION > $INSTALL_DIR/gv/version
chown -R stip:stip $INSTALL_DIR/gv

## for Apache2
cp -p $SCRIPTS_DIR/apache/stip-gv-ssl.conf /etc/apache2/sites-available
a2ensite stip-gv-ssl
