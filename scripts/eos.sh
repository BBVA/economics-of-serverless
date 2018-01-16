#!/usr/bin/env bash

APP_NAME=eos

action="$1"

function usage {
  echo "USAGE: ${0##*/} <command>"
  echo "Commands:"
  echo -e "\tbuild\t Build the app"
  echo -e "\triot\t Execute riot simulator"
  echo -e "\trun\t Run custom command inside EoS container"
}

case "$action" in
  build)
    echo -e "Building app ${APP_NAME}.."
    docker build -t local/${APP_NAME}:latest .
  ;;
  riot)
    echo -e "Running ${APP_NAME} riot.py.."
    docker run -it --rm -v $PWD:/tmp/execution -w /tmp/execution local/eos:latest
  ;;
  run)
    shift
    docker run -it --rm -v $PWD:/tmp/execution -w /tmp/execution local/eos:latest "$@"
  ;;
  *)
    usage
  ;;
esac
