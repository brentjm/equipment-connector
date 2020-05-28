FROM nodered/node-red:1.0.3-3-12-arm32v6

USER root
RUN apk add --no-cache make gcc g++ python linux-headers udev

USER node-red
WORKDIR /data
COPY flows.json settings.js package.json /data/
RUN npm install

WORKDIR /usr/src/node-red
