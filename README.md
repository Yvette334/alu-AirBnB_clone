# AirBnB Clone - The Console
## Description
This project is the first step towards building a full web application: an AirBnB clone. The goal is to create a command interpreter (similar to a shell) that can manage AirBnB objects. This includes creating, retrieving, updating, and deleting objects like Users, States, Cities, Places, etc.

## Command Interpreter
The command interpreter is built using Python's cmd module and provides a way to interact with the AirBnB objects.

## How to Start
To start the command interpreter, run the following command in your terminal:

bash
./console.py
##cHow to Use
Once the interpreter is running, you can use the following commands:

help: Show available commands and their usage

quit: Exit the interpreter

EOF: Exit the interpreter (Ctrl+D)

## Examples
Interactive Mode
bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
Non-Interactive Mode
bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
