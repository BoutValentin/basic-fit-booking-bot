# Basic Fit Booking Bot

This python program aim to book your training for you.
I'm not related to basic fit, this is an non-official usage of the booking features from basic-fit.

### Install

After forking or cloning this repositorie, you need to take a look at the ```requirements.txt``` file.
This file aim to have a lookup on the mandatory dependencies you should install.

After that, you should create a ```.env``` file, from the ```.env.example``` one.
```sh
$ cp .env.example .env
```
And edit it to add your credentials for your basic-fit account

### Usage

This bot is simple, look below :
```sh
$ python main.py <hour_your_want> <time_you_want_in_minutes>
# Ex: python main.py 06h30 60
```

### Recommendations

To automaticly make reservation for your training, you can use a VPS or an Arduino/Raspberry and create some ```cron jobs```

