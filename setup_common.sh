#!/bin/sh
INSTALL_DIR=/opt/s-tip
COMMON_DIR=/home/stip/stip-common

mkdir $INSTALL_DIR
mkdir -p $INSTALL_DIR/common
ln -s $COMMON_DIR/src $INSTALL_DIR/common/src
ln -s $COMMON_DIR/img $INSTALL_DIR/common/img
chown -R stip:stip $INSTALL_DIR
