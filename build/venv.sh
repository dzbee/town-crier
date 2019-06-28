#!/bin/bash

ENV_FILE=$1
ENV_NAME=$(head -n 1 $ENV_FILE | awk '{print $2}')

HASH=$(cat $ENV_FILE build/venv.sh | openssl sha1 | awk '{print $2}')

if [[ ! -e .venv || $(cat .venv) != *"$HASH"* ]]; then
    echo "Environment updated. Rebuilding..."

    if [[ "$PATH" == *"${ENV_NAME}/bin"* ]]; then
	echo "Shouldn't rebuild while environment is active. Run 'conda deactivate'."
	exit 1
    fi

    set -e
    if [[ -n "$(conda env list | grep $ENV_NAME)" ]]; then
	conda env remove -y -n $ENV_NAME
    fi
    conda env create -f $ENV_FILE
    echo "$HASH" > .venv
    set +e
fi
