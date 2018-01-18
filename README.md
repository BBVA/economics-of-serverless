# Economics of Serverless

## Requirements
- Pipenv (install it via 'pip install pipenv' or your distro package manager)


## Install & run

1. Install all dependencies: `$ pipenv install`  
2. Activate environment: `$ pipenv shell`
3. (optional) Run jupyter notebook `$ jupyter notebook`
4. Select and run the desired notebook.

## Contribute

Run pipenv in `dev` mode with : `pipenv install --dev`

## Docker execution environment (optional)
### Requiremens:
* Python3 + Pip
* Docker 1.12+

### Build & run EoS executor

1. Build the docker image [local/eos:latest]
```
$ ./eos build
```

2. Run the default riot.py script
```
$ ./eos riot
```

3. Run any custom command
```
$ ./eos run [command] [args] ...
```

### Executing the jupyter notebook:
1. Launch a Jupyter Docker container
  ```
  $ docker run -it --rm -p 8888:8888 -v $PWD:/home/jovyan/work jupyter/datascience-notebook
  ```
1. After that, launch a terminal inside jupyter and install awscosts package:
  ```
  $ pip install -e $HOME/work/awscosts
  ```

### Executing the jupyter notebook automated:
1. Start Jupyter server
```
$ ./eos start-jupyter
Starting eos Jupyter
6ff2af407c66ecab0a81015d5a9885a816bf69e2553c4bf2aa3962750278905f
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=1b15e1f8b8883efa272c9a5880aaf736f97b8d40f6e95ff1
```

2. Stop Jupyter server
```
$ ./eos stop-jupyter
```
