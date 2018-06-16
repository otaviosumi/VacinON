VacinON
=======

A Web App developed to help keep track of vaccination shots.


Enviroment:
----------
Developed using Python 2.7.12

Installed using "sudo pip install":
- flask 0.12.2
- pymongo 3.6.1

Requirements:
-------------

It's required to install the mongoDB:

Import the public key used by the package management system.

```sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5```

Create a list file for MongoDB.
-Ubuntu 14.04

```echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list```
-Ubuntu 16.04(our choice)

```echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list```

Reload local package database.

```sudo apt-get update```

Install the MongoDB packages.

```sudo apt-get install -y mongodb-org=3.6.5 mongodb-org-server=3.6.5 mongodb-org-shell=3.6.5 mongodb-org-mongos=3.6.5 mongodb-org-tools=3.6.5```

Developed by:
-------------

Bruno Diego Yoshikawa (bruno.diego.yoshikawa@gmail.com)

Gustavo Lima Lopes (gustavo.lima.lopes@usp.br)

Júlio César Coelho Filho (julio.coelho.filho@usp.br)

Lucas Takeru Sato (lucas.takeru.sato@usp.br)

Murilo Bellini (mhbellini95@gmail.com)

Otávio M. Sumi (otaviosumi@hotmail.com)



