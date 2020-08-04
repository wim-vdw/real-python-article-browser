#!/usr/bin/env bash

BASE_URL="https://realpython.com"

function control_c() {
  echo "Program was interrupted by the end user."
  exit
}

trap control_c SIGINT

function get_data() {
  result=$(http https://realpython.com/ | grep ic-append-from | cut -d"\"" -f4)
  echo "$BASE_URL"

  while true; do
    new="$BASE_URL$result"
    echo "$new"
    result=$(curl --silent "$new" | grep ic-append-from | cut -d"\"" -f4)
    if [ -z "$result" ]; then
      break
    fi
  done
}

get_data
