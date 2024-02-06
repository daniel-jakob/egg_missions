# Egg Missions Artifacts Visualiser

This script allows you to visualise the cumulative contents of multiple Egg, Inc. ships that returned to you.

## Example Image

<p align="center">
<img src="example_output.png" alt="output example image" width="400" alt="Sublime's custom image"/
</p>

## Install:

### Linux/Mac/Windows (with git):

```bash
git clone https://github.com/daniel-jakob/egg_missions
cd egg_missions/src
curl -O -L https://raw.githubusercontent.com/elgranjero/EggIncProtos/main/ei/python/ei_pb2.py
```

You may need to install some of the dependencies (`protobuf`, `requests`, `pillow`, etc.)

## Usage

First open up `mission.py` and put your Egg, Inc. user ID in the `EGG_API_KEY` variable. Then change the `num_ships` variable to the number of ships' contents you want to visualise.
<br>
Run the `mission.py` script. An output file (`data.json`) will be created if the script is successful.
<br>
Run the `data_vis.py` script. An image will be generated called `output_image.png`
