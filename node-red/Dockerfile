FROM nodered/node-red:1.0.1-10-minimal-arm32v6

USER root
RUN apk add --no-cache make gcc g++ python linux-headers udev

WORKDIR /data
COPY flows.json settings.js /data/
RUN chown node-red:node-red flows.json settings.js

WORKDIR /usr/src/node-red
COPY package.json /usr/src/node-red/
RUN chown node-red:node-red /usr/src/node-red/package.json 
USER node-red
RUN npm install

#CMD ["/bin/bash", "-c", "sleep 1000"]
