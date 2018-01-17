#!/usr/bin/env bash

APP_NAME=eos

action="$1"

function usage {
  echo "USAGE: ${0##*/} <command>"
  echo "Commands:"
  echo -e "\tbuild\t         Build the app"
  echo -e "\triot\t         Execute riot simulator"
  echo -e "\trun\t         Run custom command inside EoS container"
  echo -e "\tstart-jupyter\t Start Jupyter local server"
  echo -e "\tstart-jupyter\t Stop Jupyter local server"
}

function run_riot {
  docker run -it --rm -v $PWD:/tmp/execution -w /tmp/execution local/eos:latest
}

function run_custom_cmd {
  shift
  docker run -it --rm -v $PWD:/tmp/execution -w /tmp/execution local/eos:latest "$@"
}

function start_jupyter {
  docker run -d --rm --name "${APP_NAME}-jupyter" -p 8888:8888 -v $PWD:/home/jovyan/work jupyter/datascience-notebook
  docker exec -it "${APP_NAME}-jupyter" pip install -e work/awscosts
  docker logs "${APP_NAME}-jupyter"
}

function stop_jupyter {
  docker rm -vf eos-jupyter
}

case "$action" in
  build)
    echo -e "Building app ${APP_NAME}.."
    docker build -t local/${APP_NAME}:latest .
  ;;
  riot)
    echo -e "Running ${APP_NAME} riot.py.."
    run_riot
  ;;
  run)
    echo -e "Running ${APP_NAME} custom cmd"
    run_custom_cmd "$@"
  ;;
  start-jupyter)
    echo -e "Starting ${APP_NAME} Jupyter"
    start_jupyter
  ;;
  stop-jupyter)
    echo -e "Stopping ${APP_NAME} Jupyter"
    stop_jupyter
  ;;
  *)
    usage
  ;;
esac
