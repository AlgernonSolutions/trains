# Challenge One
## Purpose
Acquaint yourself with the process of finding and registering yourself with an API.
## Outcome
When you are done with this challenge, you will be able to identify your own API key and articulate an understanding of it's importance and role.
## Background
Almost all APIs (Application Program Interface) require developers to register with the API host before querying or interacting with the API. Imagine an API 
as being like a private nightclub. If you let everyone and their mule in, the place will be destroyed and you'll never get that smell out of the couches. So you solicit invitations,
register your guests, and check who they are the door. In this simple case, we will be using a pre-shared key (string of text), which we will send along with all our requests to the API.
This API key will act like our invitation, stating who we are, how many drinks we've ordered, and who to send the bill to.
### Security Point
Just like your club invitation, you should keep your API key safe and secret. If you share it, you can expect it to be abused. This can result in everything from denied API access 
to significant bills and even blacklisting.
## Process
This series of challenges utilizes the WMATA API to collect and analyze train data. Accordingly, we will need to register ourselves with the WMATA API, https://developer.wmata.com/signup/.
Provide an email address, and any other required information. When you have completed the process, you will be able to view your two keys. Navigate to the 
PRODUCTS tab, then select SUBSCRIBE. Complete the last steps and bask in their randomly generated beauty. Let them alone for now, we will deal with them more later. 
While you are on the WMATA website, take a peek at the API documentation. We will come back to this in depth, but feel free to get a preview now.