#!/bin/sh
VERSION="v0.1.0"
INSTALL_DIR=/opt/s-tip
COMMON_DIR=/home/stip/stip-common/
SCRIPTS_DIR=$COMMON_DIR/install_scripts

# git clone
git clone https://github.com/s-tip/stip-rs.git
chown -R stip:stip stip-rs

## apt install
apt install -y python-pip
apt install -y apache2 libapache2-mod-wsgi
apt install -y mysql-server libmysqlclient-dev

## pip install
pip install -r $SCRIPTS_DIR/requirements_rs.txt

# install cti-pattern-matcher from github
git clone https://github.com/oasis-open/cti-pattern-matcher.git
cd cti-pattern-matcher/
python setup.py install
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
echo $VERSION > $INSTALL_DIR/rs/version
chown -R stip:stip $INSTALL_DIR

# for Apache2
cp -p $SCRIPTS_DIR/apache/ports.conf /etc/apache2/
cp -p $SCRIPTS_DIR/apache/stip-rs-ssl.conf /etc/apache2/sites-available
sh -c "echo ServerName `hostname` > /etc/apache2/conf-available/fqdn.conf"
a2enconf fqdn
a2enmod ssl
a2ensite stip-rs-ssl

# for MongoDB
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
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