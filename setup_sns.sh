#!/bin/sh
VERSION="v0.1.0"
INSTALL_DIR=/opt/s-tip
COMMON_DIR=/home/stip/stip-common
SCRIPTS_DIR=$COMMON_DIR/install_scripts

## git clone
git clone https://github.com/s-tip/stip-sns.git
chown -R stip:stip stip-sns

## apt install
apt install -y python3-dev
apt install -y libpq-dev

## pip install
pip install -r $SCRIPTS_DIR/requirements_sns.txt

# copy SNS setting
mkdir -p $INSTALL_DIR/sns/bin
mkdir -p $INSTALL_DIR/sns/media/cache
cp -pr $COMMON_DIR/stip-sns/bin $INSTALL_DIR/sns
cp -pr $COMMON_DIR/stip-sns/media $INSTALL_DIR/sns
ln -s $COMMON_DIR//stip-sns/src $INSTALL_DIR/sns/src
cp -pr $SCRIPTS_DIR/env_sns $INSTALL_DIR/sns/.env
echo $VERSION > $INSTALL_DIR/sns/version
mkdir $INSTALL_DIR/sns/staticfiles
chown -R stip:stip $INSTALL_DIR/sns

# for Apache2
cp -p $SCRIPTS_DIR/apache/stip-sns-ssl.conf /etc/apache2/sites-available
a2ensite stip-sns-ssl

# LoadData
#export PYTHONPATH=$INSTALL_DIR/common/src:$INSTALL_DIR/rs/src:$INSTALL_DIR/sns/src
#cd $INSTALL_DIR/sns/bin
#python manage.py collectstatic --noinput
#python manage.py loaddata sns_config
#python manage.py loaddata country
#python manage.py loaddata region