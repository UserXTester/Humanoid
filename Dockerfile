# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in <https://github.com/TeamHumanoid/Humanoid>.
FROM paman7647/amanpandey:humanoid
# install main requirements.
COPY requirements.txt /deploy/
RUN pip3 install -r /deploy/requirements.txt
# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip3 install -U py-Humanoid
# clone the repo and change workdir
WORKDIR .
# start the bot
CMD ["bash", "resources/startup/startup.sh"]
