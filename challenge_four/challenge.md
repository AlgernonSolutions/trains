# Challenge Four
## Purpose
Make a call to the API and inspect the results, understanding how the returned information corresponds with the documentation.
## Outcome
Actually get some data out of the API, check it out, and correspond it with the documentation.
## Background
Whenever we use an API, our local computer/server/hamster powered doom machine sends a HTTP signal across the big beautiful internet 
to the API servers, along with some information. The API servers receive this signal, process it, and respond accordingly. It is the same process 
that happens automatically in a web browser when you visit a website.
### Provided Assets
In order to keep this challenge at the appropriate level of abstraction, we have provided an object called Conductor. The Conductor acts as the central relay point 
with the WMATA API. It will take care of the process of integrating the API key into the call, setting up the HTTP signal, and interpreting the results. Please feel 
free to tinker and improve on it.
## Process
### disclaimer
In order to test this step out, we are going to assume you have been coming to our classes, or at least trying your best to play along at home. If not, there are setup steps outside
 the scope of this documentation to run the program. Sorry, them the breaks sometime. Do not despair though, just download PyCharms https://www.jetbrains.com/pycharm/, 
 and follow their instructions to get up and running.
###
If you open the challenge folder, you will find a file labeled 'trial_api_call.py' inside. Run this file, and if all goes well, you should see a string of text in the console.
 