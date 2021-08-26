# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in <https://github.com/TeamHumanoid/Humanoid>.

FROM paman7647/amanpandey:speedo-buster-3.9

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# clone the repo and change workdir
RUN git clone https://github.com/TeamHumanoid/Humanoid.git /root/TeamHumanoid/
WORKDIR /root/TeamHumanoid/
RUN apt install -y python3.9.6
# install main requirements.
COPY requirements.txt /deploy/
RUN pip3 install -r /deploy/requirements.txt


# start the bot
CMD ["bash", "resources/startup/startup.sh"]
