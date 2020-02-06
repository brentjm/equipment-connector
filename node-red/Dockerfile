FROM arm32v7/node:buster

COPY group /etc/group

USER node

RUN mkdir "${HOME}/.npm-packages"\
    && cd "${HOME}/.npm-packages"\
    && npm config set prefix "${HOME}/.npm-packages"\
    && echo "NPM_PACKAGES=${HOME}/.npm-packages" >> "${HOME}/.bashrc"\
    && echo "export PATH=$PATH:${HOME}/.npm-packages/bin" >> "${HOME}/.bashrc"\
    && /bin/bash -c "source ${HOME}/.bashrc"\
    && mkdir "${HOME}/.node-red"\
    && npm install -g node-red

COPY package.json /home/node/.node-red/
WORKDIR /home/node/.node-red
RUN npm install
COPY settings.js /home/node/.node-red/
COPY flows.json /home/node/.node-red/

CMD ["/home/node/.npm-packages/bin/node-red"]
