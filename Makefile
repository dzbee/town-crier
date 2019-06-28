SHELL=/bin/bash

VENV=conda activate town-crier &&

# Build

venv: build/environment.yml build/venv.sh
	build/venv.sh build/environment.yml && touch .venv
