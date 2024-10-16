# YGT Workshop - Into to Game Development with Python and PyGame

Welcome to the Young Gifted Techie Workshop page! This workshop is designed to give a basic introduction to game development using python and the pygame library.

## Computer Setup

To ensure you are ready to participate in the workshop, please follow the steps to get python and pygame installed on your computer.

1. **Python Install - Windows**

    Python must be installed to participate in the workshop. To install python on a windows computer, you can use the Microsoft Store application and search for "Python". I am using "Python 3.11" for this workshop.

    <img src="./img/README/ms-store.png" alt="Microsoft Store App" width="400"/>
    <img src="./img/README/ms-store-python.png" alt="Microsoft Store App - Python 3" width="400"/>


    After installing, open a command line terminal (Windows Powershell) and run the following to check that you have python version 3.11 installed.

    `python3 --version`

    You should see the version of Python show up in Powershell. Anything matching "Python 3.11" is ok (3.11.7 or 3.11.9 are fine for this workshop).

<img src="./img/README/python-version.png" alt="Python Version" width="500"/>

1. **Python Install - Mac**

    Python installation for Mac computers can be done using the python installer for Mac. Visit [https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/) to download Python version 3.11.9 for Mac. You want to scroll to the bottom of the page and select "macOS 64-bit universal2 installer"

   <img src="./img/README/mac-python.png" alt="Mac Python" width="700"/>

   After installing, open the terminal application and run this command to check python version. 
   
   `python3 --version`

   You should see the version of Python show up. Anything matching "Python 3.11" is ok (3.11.7 or 3.11.9 are fine for this workshop).

2. **Pip Install**

    Now that we have python installed, lets open a terminal and make sure we have `pip3` installed as well. Pip is the package manager for Python packages. This is what we will use to install libraries to use in this workshop. Pip should be pre-installed when installing python3 for Windows or Mac. 

    To check if pip is already installed, run this command from a terminal (Windows Powershell for windows or Terminal program for Mac)

    `pip3 --version`

    If you get some sort of output showing the pip version, you are good to go! 

    <img src="./img/README/pip.png" alt="Pip"/>

    If you get an error that pip is not found, try the following command to install pip.

    `python3 -m ensurepip`

    After running this, try to check the pip version again to verify installation.

3. **PyGame Install**

    PyGame is a library that we are going to be using during this workshop. Lets install the pygame library using pip and ensure that it is installed correctly. 

    To install pygame, run the following command in a terminal:

    `pip3 install pygame`

    Once that is run, we can verify the install was correct using this next command:

    `python3 -m pygame.examples.aliens`

    When running this last command, a game window should pop up with a simple game of a car moving on the ground. If this is working, you are ready to go!

    <img src="./img/README/example-game.png" alt="Example Game" width="300"/>
