FROM nodered/node-red:1.0.3-3-12-arm32v6

USER root
RUN apk add --no-cache make gcc g++ python linux-headers udev
# TODO
# write sed script to add node-red to dialout in /etc/group

COPY package.json /usr/src/node-red/
RUN npm install

COPY settings.js flows.json /data/
RUN chown -R node-red:node-red /data
USER node-red
