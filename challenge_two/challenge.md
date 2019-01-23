# Challenge Two
## Purpose
Learn how to store your API keys securely, access them, and use them to make your first API call.
## Outcome
Describe a simple method to secure your API key, and then access it from your application. 
## Background
Now that we have generated our keys, let us find an easy way to store them safely. For this example, I have stored some invalid keys in a file 
called keys.txt. DO NOT DO THIS. When we share this project on GitHub, those keys will go with them. So unless we want our neighbors, our neighbors neighbors, and 
Bryce from those irritating commercials using our account, we need a better place to store them. 
## Process
The easiest place to store simple credentials is in your home directory. On a Windows computer, this is the place where your documents automatically save and
your downloads store by default. This folder is generally encrypted by default, and is thus an excellent place to store these keys. 
Open up your home folder, and take a look around. If you can't find it, try opening a file browser and typing 
"C:\Users\". The folder which opens up should have a list of all the people who use the computer. Open the file with your name on it.
Inside of the folder, create a new folder named "algernon_challenge". The spelling is important here, so if you change it, make a note of it.
Open a text editor, Notepad is just fine, and copy and paste the keys you generated in the previous challenge. Put one on each line, like the example we have here.
When you are done, save the file as keys.txt within your newly made folder. With this process done, our program can now reliably predict 
where the keys will be, but those keys will not be shared through version control.