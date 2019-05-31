#!/usr/bin/env bash

usage () {
cat << EOF
Usage: Run nbconvert and optionally serve presentation.
Options:
 -h,--help: show this message
 -s,--serve: serve the file
EOF
exit
}

if [[ $# -eq 0 ]]; then
  echo "Must supply an argument!"
  usage
fi

SERVE=
while [[ $# -gt 0 ]]; do
  key="${1}"
  case ${key} in
    -h|--help)
      usage ;;
    -s|--serve)
      SERVE=1
      shift ;;
    *)
      notebook=$(basename ${1} .ipynb).ipynb
      shift ;;
  esac
done

if [ ! -z "${SERVE}" ]; then
  jupyter nbconvert --to slides ${notebook} --reveal-prefix=reveal.js --post serve
else
  jupyter nbconvert --to slides ${notebook} --reveal-prefix=reveal.js
fi
