FROM nodered/node-red:1.0.3-3-12-arm32v6

USER root
RUN apk add --no-cache make gcc g++ python linux-headers udev

COPY package.json /usr/src/node-red/
RUN npm install

USER node-red
COPY settings.js flows.json /data/
