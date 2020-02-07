from python:3.6

RUN useradd -rm -d /home/aws -s /bin/bash -U -u 1000 aws
USER aws

WORKDIR /home/aws
RUN curl https://www.amazontrust.com/repository/AmazonRootCA1.pem -o root-CA.crt\
    && git clone https://github.com/aws/aws-iot-device-sdk-python.git\
    && mkdir python


USER root
RUN cd /home/aws/aws-iot-device-sdk-python\
    && python setup.py install

USER aws
COPY root-CA.crt /home/aws/ 
COPY test.sh connected-chiller-01.cert.pem connected-chiller-01.private.key connected-chiller-01.public.key device_registration.py setup_helper.py chiller_mon.py /home/aws/python/

CMD ["/bin/bash", "-c", "sleep 10000"]
