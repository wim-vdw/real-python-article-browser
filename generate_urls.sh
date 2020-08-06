#!/usr/bin/env bash

# Generate a list with URLS containing references to all Real Python articles.
# No arguments are needed.
# Result can be dumped in a TXT file to be used as input for the Python program.

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
