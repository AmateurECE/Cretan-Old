# Cretan

## A Server Monitor for Android

Follow this project on its Trello board,
[here](https://trello.com/b/pqHcdNMn/cretan)!

_Cretan_ is a system for sending notifications to mobile devices from
server-side applications, built using Firecloud Messaging.

## Navigating This Repository and Building

The three major branches of this repository each contain one of the three
components of the system. The branches are named `master;` followed by the name
of the component. Instructions for building each component are given below:

1. User Server
```
git checkout 'master;user-server'
cmake -S . -B build
cd build
make
```