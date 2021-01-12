# MeteoPipe Lib
 Project under development

More github repo for MeteoPipe app:
* [MeteoPipeWebsite](https://github.com/rozek1997/meteopipe)
* [MeteoPipe serverless logic backend](https://github.com/rozek1997/meteopipe-serverless-backend)
# Description

Library for connecting to MeteoPipe application developed and deployed on AWS. Library is based on Paho MQTT 
Lib for Python, which made my life easier to connect to AWS IoT core broker than using dedicated AWS IoT SDK. 
For connecting to broker library require configuration file with attributes such as:
* clientId
* endpoints
* topics
* path to X.509 cert and private keys
* and more

The example of configuration you can find in samples folder

To connect to AWS IoT broker from that client lib you need to register your device on
[MeteoPipe website](https://github.com/rozek1997/meteopipe). The device will be provisioned in AWS IoT Core Thing
Registry and then application will return personal X509 cert, public key, private key, CA bundle certs and personal 
config file. With those files you can connect any device you want to MeteoPipe and send any data you wish from 
your device .It is worth keep in mind that configuration file need have attribute of location. It is crucial 
for the MeteoPipe Website to properly display localisation and statistics of yours device. 