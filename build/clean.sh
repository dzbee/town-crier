#!/bin/bash

if [[ $(find . -iname "*~") ]]; then find . -iname "*~" | xargs rm; fi
if [[ $(find . | grep .py[co]) ]]; then find . | grep .py[co] | xargs rm -rf; fi
