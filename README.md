
# TorogOS Linux Drivers/CODECS installer

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/m0rniac/torogos-drivers/blob/main/LICENSE)
## Installation of VENV (Recommended)

Install virtual environment on Linux (TorogOS based):

```bash
sudo apt install python3-venv
```
```bash
pip3 install virtualenv
``` 


## Cloning repository including VENV

- Linux (TorogOS based):
```bash
python3 -m venv torogos-drivers && source torogos-drivers/bin/activate && git clone https//github.com/m0rniac/torogos-drivers temp_folder && mv temp_folder/* . && rm -r temp_folder && deactivate
```
```bash
cd torogos-drivers/
```
```bash
source bin/activate
```
```bash
pip3 install -r requirements.txt
```

## Run CLI (only in a Console)
- Terminator as default console in TorogOS:
```bash
python3 main.py
```
# Download already builded package:

- You can download an already builded version of 'TorogOS Drivers' [by clicking here :D](https://github.com/m0rniac/torogos-drivers/releases)


.
## Feedback
If you have any feedback, please reach out to me at:

[![instagram](https://img.shields.io/badge/instagram-0A66C2?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/christcastr/)

[![portfolio](https://img.shields.io/badge/buy_me_a_coffee-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.paypal.com/paypalme/christcastr/)
