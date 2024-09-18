### Setting Up Your Environment

To get started with this project, you'll need to install a few dependencies. Follow these steps to set up your environment:

**Step 1: Install Selenium**

Open your terminal and run the following command to install Selenium:
```
pip install selenium
```
**Step 2: Install Chrome Web Driver**

Next, you'll need to install the Chrome web driver. Run the following commands in your terminal:
```
sudo apt-get update
sudo apt-get install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```
**Step 3: Install Virtual Display (Optional)**

If you want to run your script in a virtual display, you'll need to install `pyvirtualdisplay` and some additional dependencies. Run the following commands:
```
pip install pyvirtualdisplay
sudo apt-get update
sudo apt-get install -y xvfb x11-utils
```
Note: This step is optional and might not be necessary for your project.
