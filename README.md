This repo contains code for building and deploying an application that allows RPG game masters to design limited encounters that individual players may adventure through asynchronously. This could be used for running individual encounters in between game sessions, for establishing a campaign world or new characters, or even running an entire adventure.

This repo is a work in progress, and until 0.1.0 may describe a plan of execution rather than the actual state of the application.

The player is presented with written scenarios and a list of options. Each choice directs them to a new scenario. This is implemented using a character model stored in a database and dynamically generated endpoints. Currently there are no models for character history, making the adventure essentially a Markov chain.

The game master can design encounters by completing a form with a scenario, choices, and the scenario IDs the choices direct players to (if any). Additionally scenarios and choices can be conditioned on the player model.