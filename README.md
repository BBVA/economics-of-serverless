# Economics of Serverless

## Requirements
- Pipenv (install it via 'pip install pipenv' or your distro package manager)


## Install & run

1. Install all dependencies: `$ pipenv install`  
1. Activate environment: `$ pipenv shell`
1. (optional) Run jupyter notebook `$ jupyter notebook`
1. Enable widgets in Jupyter: `$ jupyter nbextension enable --py widgetsnbextension`
1. Select and run the desired notebook.

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

Contributing to Economics of Serverless
=========================

You can contribute to Economics of Serverless in a few different ways:

- Submit issues through [issue tracker](https://github.com/BBVA/Economics-of-Serverless/issues) on GitHub.
- If you wish to make code changes, or contribute something new, please follow the
[GitHub Forks / Pull requests model](https://help.github.com/articles/fork-a-repo): fork the
[Economics of Serverless](https://github.com/BBVA/Economics-of-Serverless/), make the changes and propose it back by submitting a pull request.

License
=======

This project is distributed under [Apache License](https://github.com/BBVA/Economics-of-Serverless/blob/master/LICENSE)
