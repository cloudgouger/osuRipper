# osuRipper
osuRipper looks through your osu Lazar data folder to find metadata files. It will eventually use these to generate you a list of beatmaps you have installed and a link to them. Currently, it only finds metadata files and packs them up to a zip.

Right now, the main focus is gathering more data and researching the metadata layout between osu file format versions. Feel free to run this on your own machine and send me the .zip file. It uses standard python libraries (shutil, pathlib, & os), and should do 99% of the work for you, you just need the path to your osu data folder.
