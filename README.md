# median-fire-away

A simple python script for sending test requests to [median-microservice](https://github.com/respondcreate/median-microservice).

## Installation

This script is not available on pip so, to get it on your local machine you'll need to clone it down from github:

```bash
$ git clone git@github.com:respondcreate/median-fire-away.git
```

Now, change into the directory you just cloned:

```bash
$ cd median-fire-away/
```

## How it works

Using this script is super-easy:

```bash
$ python launch.py
```

Running the above command will send 2000 random integers between 1 and 100,000 to the `median-microservice` /put endpoint. If you want to change the amount of requests or upper-limit range just use the command line options below.

### Command Line Options

* `-a, --amount <amount>`

    An integer representing the amount of /put requests you want to send.

    **Default:** `2000`

* `-u, --upper-limit <upper_limit>`

    The largest integer to send to /put (each number sent will be randomly chosen between 1 and this value).

    **Default:** `100000`

So, if you wanted to send 100 put requests between 1 and 20 you'd run this:

```bash
$ python launch.py -a 100 -u 20
```
