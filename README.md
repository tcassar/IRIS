
# IRIS

**[*Winning project*](https://developer.sony.com/posts/here-are-the-winning-projects-of-the-spresense-hackathon-at-the-university-of-manchester) at the Sony X University of Manchester Hackathon, June 2022**

![Image with IRIS logo, and computer tracking visuals overlayed on a person](https://github.com/tcassar/IRIS/blob/master/img/iris-cover-img.png)

---
## About

IRIS was built with the visually impaired in mind. 

*"OK, IRIS - describe my surroundings to me"*

On hearing a prompt such as this, IRIS will use its onboard camera to take an image of your surroundings. It then gives you a narrated audio-visual (AV) description of what is going on around you through an earpiece. 

---
## What we did

As a team of four, with only seven hours to go from inception to implementation, we split the work effectively.

[Ioan](https://www.linkedin.com/in/ioan-gwenter-4b351227b/) assembled the hardware (a Spresence board, WiFi module, camera and microphone), as well as working on producing a pitch to showcase the project. [Tom Hewitt](https://www.linkedin.com/in/tomdhewitt/) worked on the code running on the board, including setting up communications with IRIS's server. [Lourenço](https://www.linkedin.com/in/lourencofsilva/) trained a model to listen for the wake word, *"Ok, IRIS"*, using [Edge Impulse](https://edgeimpulse.com/). [Tom Cassar](https://www.linkedin.com/in/tom-cassar) built a server which made calls to OpenAI's GPT3 and Google Cloud API to convert the raw data from the board into a narrated AV description. 

