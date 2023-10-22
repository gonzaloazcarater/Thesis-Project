# Thesis-Project
Final Thesis Project: Development of a tool for realistic network traffic generation and orchestration based on user behavior.
# Description
The general objective of this project is focused on the generation of realistic user traffic, 
firstly, a study of the different traffic generation tools used in the Internet will be carried out. 
Given the characteristics of the project, emphasis will be placed on tools focused on the generation of network traffic based on user behavior.

In order to generate this traffic, we propose the use of the NPC (NonPlayer Character) simulation tool GHOSTs, which allows simulating users, as well as their behavior through different configuration files. The purpose of using this tool is focused on the integration of these simulated users in CyberRange training platforms.

Taking into account the above mentioned, the development of this project will consist of, given a file describing the network topology, analyzing it and implementing a logic for the generation of behavioral models obtaining a realistic traffic simulation through those simulated users.

The objective in the development phase will be to generate behavioral files, which will be sent in a pseudo-random way or with a programmed logic from an orchestrator machine to the different machines that have the GHOSTs client. In order to carry out the distribution and execution of the traffic models, the use of the MQTT messaging protocol is proposed.
# Autor
Gonzalo Azcarate Rodriguez
