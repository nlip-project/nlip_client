This repository is part of the set of repositories implementing python based NLIP Proof of Concept Implementation: 

# Python NLIP Repositories 

This repository contains one component of the various python repositories for NLIP implementation. The various repositories are: 

* nlip_sdk: this provides a software development kit in python that implements the abstractions of NLIP message, submessages along with a factory to ease the creation of NLIP messages and submessages 
* nlip_client: this provides a package that simplifies the task of sending NLIP messages using the base underlying protocol. The current implementation uses httpx as the base transfer package. 
* nlip_server: this provides a paclage that simplifies the task of writing a server-side NLIP application. This provides the abstractions of a NLIPApplication and a NLIP Session. An application consists of multiple sessions. 

The above three are the components needed to write a client or a server. To write a client, you need to use nlip_sdk and nlip_client. To write a server side application, you need to use nlip_sdk and nlip_server. 

The following repositories contain a few simple clients and server side applications: 

* nlip_soln: this provides a few simple prototype server side solutions using the nlip_server package 
* text_client: this provides a simple text based chatbot to interface with a NLIP server 
* kivy_client: this provides a python kivy based visual client to interact with an NLIP server

# nlip_client
 A python client for nlip

This is a library wrapper that allows for development of various NLIP clients.
This version supports httpx as the base transfer protocol. 
