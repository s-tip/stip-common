#!/bin/sh
INSTALL_DIR=/opt/s-tip
COMMON_DIR=/home/stip/stip-common/
SCRIPTS_DIR=$COMMON_DIR/install_scripts

# Ubuntu check
if [ -f /etc/lsb-release ]; then
    . /etc/lsb-release
    echo "Ubuntu Codename: $DISTRIB_CODENAME"
    if [ $DISTRIB_CODENAME = "focal" ]; then
        echo "Distribution focal detected. Use BIONIC mongo package instead of focal temporarily."
        DISTRIB_CODENAME=bionic
    fi
else
    echo "This script only works on Ubuntu."
    exit 1
fi

# git clone
git clone https://github.com/s-tip/stip-rs.git
chown -R stip:stip stip-rs

## apt install
apt install -y python3-pip
apt install -y apache2 libapache2-mod-wsgi-py3
apt install -y mysql-server libmysqlclient-dev libssl-dev

## pip install
pip3 install -r $SCRIPTS_DIR/requirements_rs.txt

# install cti-pattern-matcher from github
git clone https://github.com/oasis-open/cti-pattern-matcher.git
cd cti-pattern-matcher/
python3 setup.py install
cd -
chown -R stip:stip cti-pattern-matcher

# copy RS setting
mkdir -p $INSTALL_DIR/rs/bin
mkdir -p $INSTALL_DIR/rs/community
mkdir -p $INSTALL_DIR/rs/data
mkdir -p $INSTALL_DIR/rs/staticfiles
ln -s $COMMON_DIR/stip-rs/src $INSTALL_DIR/rs/src
cp -p $COMMON_DIR/stip-rs/bin/* $INSTALL_DIR/rs/bin/
cp -p $COMMON_DIR/stip-rs/data/* $INSTALL_DIR/rs/data/
cp -p $SCRIPTS_DIR/env_rs $INSTALL_DIR/rs/.env
ln -s $COMMON_DIR/stip-rs/version $INSTALL_DIR/rs/version
chown -R stip:stip $INSTALL_DIR

# for Apache2
cp -p $SCRIPTS_DIR/apache/ports.conf /etc/apache2/
cp -p $SCRIPTS_DIR/apache/stip-rs-ssl.conf /etc/apache2/sites-available
sh -c "echo ServerName `hostname` > /etc/apache2/conf-available/fqdn.conf"
a2enconf fqdn
a2enmod ssl
a2ensite stip-rs-ssl

# for MongoDB 4.0
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb http://repo.mongodb.org/apt/ubuntu $DISTRIB_CODENAME/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
apt update
apt install -y mongodb-org
systemctl start mongod
systemctl enable mongod

# init MySQL
echo "-- init MySQL --"
## copy my.conf (charset=utf-8)
cp -p $SCRIPTS_DIR/my.cnf /etc/mysql/my.cnf
service mysql restart

mysql -p -u root -e 'create database s_tip;'
## (Enter passwd 'root')

## Grant all privileges on s_tip.* to stip@"%" identified by 'stip' with grant option;
mysql -p -u root < $SCRIPTS_DIR/init_mysql.sql
