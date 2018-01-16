# Economics of Serverless

### Requiremens:
* Python3 + Pip
* Docker 1.12+

### Build & run EoS executor

1. Build the docker image [local/eos:latest]
```
./eos build
```

2. Run the default riot.py script
```
./eos riot
```

3. Run any custom command
```
./eos run [command] [args] ...
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

# To-Do:
- *Urgent* Install package in container's entrypoint
