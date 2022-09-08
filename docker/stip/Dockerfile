FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# apt install
## for docker image
RUN apt update && apt install -y \
    git python3.8 sudo dialog wget
## for stip-rs & stip-sns
RUN apt install -y \
    python3-pip apache2 libapache2-mod-wsgi-py3 libmysqlclient-dev mysql-client python3-dev libpq-dev libssl-dev \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*
RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add -
RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list
RUN apt update && apt install -y \
    mongodb-org \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*
RUN apt update && apt install -y systemd

# env
ENV INSTALL_DIR=/opt/s-tip \
    COMMON_DIR=/stip-common
ENV SCRIPTS_DIR ${COMMON_DIR}/install_scripts

# pip install
WORKDIR /
RUN git clone https://github.com/s-tip/stip-common.git
RUN pip3 install -r ${SCRIPTS_DIR}/requirements_rs.txt -r ${SCRIPTS_DIR}/requirements_gv.txt -r ${SCRIPTS_DIR}/requirements_sns.txt -r ${SCRIPTS_DIR}/requirements_txs2.txt

# stip-common setup
RUN mkdir -p ${INSTALL_DIR}/common
RUN ln -s ${COMMON_DIR}/src ${INSTALL_DIR}/common/src && ln -s ${COMMON_DIR}/img ${INSTALL_DIR}/common/img

# stip-rs setup
WORKDIR /stip-common
RUN git clone https://github.com/s-tip/stip-rs.git
RUN mkdir -p ${INSTALL_DIR}/rs/bin ${INSTALL_DIR}/rs/community ${INSTALL_DIR}/rs/data ${INSTALL_DIR}/rs/staticfiles ${INSTALL_DIR}/rs/conf
RUN ln -s ${COMMON_DIR}/stip-rs/src ${INSTALL_DIR}/rs/src
RUN cp -p ${COMMON_DIR}/stip-rs/bin/* ${INSTALL_DIR}/rs/bin/ && cp -p ${COMMON_DIR}/stip-rs/data/* ${INSTALL_DIR}/rs/data/ && cp -p ${SCRIPTS_DIR}/env ${INSTALL_DIR}/.env && cp -p ${COMMON_DIR}/stip-rs/conf/* ${INSTALL_DIR}/rs/conf/
RUN ln -s ${INSTALL_DIR}/.env ${INSTALL_DIR}/rs/.env
RUN ${INSTALL_DIR}/rs/bin/setup_env.py ${INSTALL_DIR}/.env
RUN cp -p ${SCRIPTS_DIR}/apache/ports.conf /etc/apache2/ && cp -p ${SCRIPTS_DIR}/apache/stip-rs-ssl.conf /etc/apache2/sites-available
RUN sh -c "echo ServerName `hostname` > /etc/apache2/conf-available/fqdn.conf"
RUN a2enconf fqdn
RUN a2enmod ssl
RUN a2ensite stip-rs-ssl
RUN mkdir /var/log/audit

# stip-gv setup
WORKDIR /stip-common
RUN git clone https://github.com/s-tip/stip-gv.git
RUN mkdir -p ${INSTALL_DIR}/gv/bin ${INSTALL_DIR}/gv/conf ${INSTALL_DIR}/gv/staticfiles ${INSTALL_DIR}/gv/stix
RUN ln -s ${COMMON_DIR}/stip-gv/src ${INSTALL_DIR}/gv/src
RUN cp -p ${COMMON_DIR}/stip-gv/bin/* ${INSTALL_DIR}/gv/bin/ && cp -p ${COMMON_DIR}/stip-gv/conf/* ${INSTALL_DIR}/gv/conf
RUN ln -s ${INSTALL_DIR}/.env ${INSTALL_DIR}/gv/.env
RUN cp -p ${SCRIPTS_DIR}/apache/stip-gv-ssl.conf /etc/apache2/sites-available
RUN a2ensite stip-gv-ssl

# stip-sns setup
WORKDIR /stip-common
RUN git clone https://github.com/s-tip/stip-sns.git
RUN mkdir -p ${INSTALL_DIR}/sns/bin ${INSTALL_DIR}/sns/media/cache ${INSTALL_DIR}/sns/staticfiles
RUN cp -pr ${COMMON_DIR}/stip-sns/bin ${INSTALL_DIR}/sns && cp -pr ${COMMON_DIR}/stip-sns/media ${INSTALL_DIR}/sns && cp -p ${SCRIPTS_DIR}/apache/stip-sns-ssl.conf /etc/apache2/sites-available
RUN ln -s ${INSTALL_DIR}/.env ${INSTALL_DIR}/sns/.env
RUN ln -s ${COMMON_DIR}/stip-sns/src ${INSTALL_DIR}/sns/src
RUN a2ensite stip-sns-ssl

# stip-txs2 setup
WORKDIR /stip-common
RUN git clone https://github.com/s-tip/stip-txs2.git
RUN mkdir -p ${INSTALL_DIR}/txs2/bin ${INSTALL_DIR}/txs2/staticfiles
RUN cp -pr ${COMMON_DIR}/stip-txs2/bin ${INSTALL_DIR}/txs2 && cp -p ${SCRIPTS_DIR}/apache/stip-txs2-ssl.conf /etc/apache2/sites-available && cp -p ${SCRIPTS_DIR}/apache/stip-txs2-console-ssl.conf /etc/apache2/sites-available
RUN ln -s ${INSTALL_DIR}/.env ${INSTALL_DIR}/txs2/.env
RUN ln -s ${COMMON_DIR}/stip-txs2/src ${INSTALL_DIR}/txs2/src
RUN a2ensite stip-txs2-ssl
RUN a2ensite stip-txs2-console-ssl

# modification for docker image
## mysql/mongo hostname
RUN echo "MYSQL_HOST=mysql" >> ${INSTALL_DIR}/.env
RUN sed -i".org" 's/"host": "localhost"/"host": "mongo"/g' ${COMMON_DIR}/stip-rs/src/ctirs/fixtures/mongo.json
RUN sed -i".org" 's/"circl_mongo_host": "localhost"/"circl_mongo_host": "mongo"/g' ${COMMON_DIR}/stip-rs/src/ctirs/models/sns/config/fixture/sns_config.json
RUN sed -i 's/"attck_mongo_host": "localhost"/"attck_mongo_host": "mongo"/g' ${COMMON_DIR}/stip-rs/src/ctirs/models/sns/config/fixture/sns_config.json

# create stip user
RUN adduser --disabled-password --gecos "" stip && adduser stip stip
RUN gpasswd -a stip sudo && gpasswd -a stip adm
RUN chown -R stip:stip ${INSTALL_DIR}
RUN chown -R stip:stip ${COMMON_DIR}
RUN chown -R stip:stip /var/log/audit
