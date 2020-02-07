#!/bin/bash

# run pub/sub sample app using certificates downloaded in package
printf "\nRunning pub/sub sample application...\n"
python "/home/aws/aws-iot-device-sdk-python/samples/basicPubSub/basicPubSub.py" -e a5o79rpm1kyz5-ats.iot.us-east-1.amazonaws.com -r ../root-CA.crt -c connected-chiller-01.cert.pem -k connected-chiller-01.private.key -M "1" -t "chillers/connected-chiller-01/status"
