# Chrome Dinosaur Game

For this project you are playing the typical chrome dinosaur game except that you have additional ability to shoot fireballs.

## Motivation

This is based of the classic T-Rex Dinosaur Game that you played when opened your browser and realised you had no internet. However, the thing is that game was too easy so to make it more challenging the trees and pterodactyl are now able to spawn more randomly and could be grouped together much closer. This would be a bit too difficult of course since you wouldn't make it far so you have the ability to shoot fireballs too. You are only allowed to shoot three fireballs at a time and there is a waiting period between each fireball to be shot. Just know that this game requires both luck and skill to get far.

## Getting Started

### Prerequisites

- [python](https://www.python.org/downloads/)
- pygame module

#### Installing prerequisitees on Windows
1. Click on the link on python which will take you to the downloads page and download the latest version of python
2. Find where you downloaded the installer to and click on the installer to download python
3. Check what version of python you are using by opening up command prompt and type in

        python --version

    If you have any version of python 3.x.x then you are good to continue.

4. To install the pygame module you need to make sure that you have pip first. To check open up command prompt and type in

        pip --version

    If you have pip great and if it asks you to update pip then follow the steps that it shows you. If you do not have pip installed then you can follow this [installation](https://www.liquidweb.com/kb/install-pip-windows/) guide.

5. Once you have pip and python. You can install pygame by opening command prompt and typing in

        pip install pygame

#### Installing prerequisites on Ubuntu/Debian
1. First install python by opening up the terminal and enter the command

        sudo apt-get install python3.8

2. Check that pip is install by typing in

        pip3 –version

    If pip doesn't exist then enter the command below and check the version by doing

        sudo apt install python3-pip
        pip3 -V

3. Install pygame by entering the command below in terminal

        sudo apt-get install python3-pygame

### Installing
1. You can either download the zip file and unzip it or clone the repository

        git clone https://github.com/TvDragon/chrome_dinosaur_game_python.git

## Usage

1. Once you have installed the prerequisites, unzipped the file or cloned the repository move into the folder
2. Open up command prompt or a terminal and enter the one of the commands below and you can start playing

        python3 main.py
        python main.py

## Controls

- Jump - up arrow key
- Shoot fireball - space bar
