## RPC Communication between two django projects

### There are two django projects in this repository.

1. The user project;
2. The currency project

The project uses Remote-Procedure-Calls to communicate with each other synchronously.

This communication simply simulates the scenario whereby if a user is being created 
in the User Project, two currencies (Nigerian Naira and United States Dollars) are automatically being created for that user.

Because the Currency Project is being hosted on a different server entirely (by simulation),
It is impossible to create the Currency object from the User project, so without knowing the 
Model name, nor the defined fields, and without any prior knowledge of the Currency project 
and it's model, two default currencies will still be created for every user created from the
user project.


#### How to run the project
Run the user project as a seperate django project with it's own apps
User Project
```
python manage.py runserver
```


Run the currency project as a seperate django project with it's own apps.
Currency Project
```
python manage.py runserver 0.0.0.0:50051
```

In another terminal;
```
python server.py
```

And whenever you create a user from the User project running anywhere in the world, the Currency 
project running in another part of the world on a different node or edge will automatically create 
two currencies for that newly created user - one Naira currency and another USD currency.


Happy Tweaking to your liking.
:)
