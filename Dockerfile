# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in <https://github.com/TeamHumanoid/Humanoid>.
FROM python:3.9
FROM paman7647/amanpandey:speedo-buster-3.9
# install main requirements.
COPY requirements.txt /deploy/
RUN pip3 install -r /deploy/requirements.txt
# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip3 install -U py-Humanoid
# clone the repo and change workdir
RUN git clone https://github.com/TeamHumanoid/Humanoid.git /root/TeamHumanoid/
WORKDIR /root/TeamHumanoid/
# start the bot
CMD ["bash", "resources/startup/startup.sh"]
