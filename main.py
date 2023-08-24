"""
MIT License

Copyright (c) [2023] [@m0rniac]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import time
import colorama
import platform

from screen import Logos
from menu import Bar

def is_supported_os():
    if platform.system() == 'Linux':
        with open('/etc/os-release', 'r') as os_release_file:
            for line in os_release_file:
                if line.startswith('ID=debian'):
                    return True
    return False

if not is_supported_os():
    print(colorama.Fore.RED + colorama.Style.BRIGHT)
    print("[TorogOS; Error durante la ejecución]:")
    print("- Sistema operativo no soportado, asegúrate de estar en una versión de TorogOS Linux o Debian.")
else:
    os.system('clear')
    def app():
        time.sleep(0.5)
        Logos.torogos()
        time.sleep(1)
        Bar.menu()

    if __name__ == "__main__":
        app()