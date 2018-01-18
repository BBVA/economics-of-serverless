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

### Executing the jupyter notebook:
1. Launch a Jupyter Docker container
  ```
  $ docker run -it --rm -p 8888:8888 -v $PWD:/home/jovyan/work jupyter/datascience-notebook
  ```
1. After that, launch a terminal inside jupyter and install awscosts package:
  ```
  $ pip install -e $HOME/work/awscosts
  ```