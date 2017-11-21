
# Executing the jupyter notebook:
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
