# OculusD IoT Administration Library for AWS IoT

This library collection intend to ease your management of IoT projects that will integrate with AWS IoT.

The following functionality is provided by this library:

* Define Things
  * Persist the Thing definition in DynamoDB
  * Persist a local copy of thing definitions
* Setup the required certificates and policies
* Get IoT end-point URL for the AWS Account
  * Persist locally
* Create the resources required for logging sensor data
* Create the resources required for state management, triggers and actions
  
This library could also be used to retrieve a complete copy of all thing definitions from the DynamoDB table containing the definitions.
