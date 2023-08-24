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

import sys
import colorama
import subprocess


class TorogOS:
    """
    [Corpus; DRIVERS]
    """
    def drivers_graphics():
        color_red = colorama.Fore.RED + colorama.Style.BRIGHT
        color_cyan = colorama.Fore.CYAN + colorama.Style.BRIGHT
        color_green = colorama.Fore.GREEN + colorama.Style.BRIGHT
        color_white = colorama.Fore.WHITE + colorama.Style.BRIGHT
        color_yellow = colorama.Fore.YELLOW + colorama.Style.BRIGHT
        color_reset = colorama.Fore.RESET + colorama.Style.RESET_ALL
        
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])
        request = "apt-cache search ^xserver-xorg-video-"
        output = subprocess.check_output(request, shell=True, text=True)
        package_list = output.strip().split('\n')
        
        package_names = [package.split()[0] for package in package_list]
        
        def install_packages(package_names):
            try:
                install_command = f"sudo apt-get install -y {' '.join(package_names)}"
                subprocess.run(install_command, shell=True, check=True)
                
                print(color_cyan)
                print("[TorogOS; Paquete instalado correctamente]")
                
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
            except subprocess.CalledProcessError as Log:
                print(color_red)
                print("[TorogOS; Ocurrió un error durante la instalación del paquete]")
                print('- Registro de error:\n')
                print(Log)
        
        print(color_green)
        print('[TorogOS; Lista de drivers/paquetes gráficos disponibles para su equipo]:')
        print(color_yellow + "==============================================" + color_reset)
        print(package_names)
        print(color_yellow + "==============================================" + color_reset)
        
        print(color_cyan)
        print('¿Desea iniciar con la instalación? (s/n)')
        usr = input(str('[>>]: '))
        print("OK")
        
        if usr == 's' or usr == '':
            step_size = 1
            for i in range(0, len(package_names), step_size):
                package_chunk = package_names[i:i+step_size]
                install_packages(package_chunk)
            print(color_cyan)
            subprocess.run('sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y', shell=True, check=True)

            print(color_green)
            print('\n\n[TorogOS; Instalación finalizada]')
            
            print(color_yellow + "==============================================" + color_white)
            print("ADVERTENCIA:")
            print('- Para efectuar el funcionamiento de los drivers/paquetes que acabas de instalar debes reiniciar el equipo.\n')
            print('- Solo instalaste UNA categoría de drivers/paquetes, vuelve a ejecutar el instalador y asegúrate de instalar todas las categorías necesarias para tu equipo.')
            print(color_yellow + "==============================================" + color_reset)
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()
        else:
            print(color_red)
            print('[TorogOS; Instalación cancelada]')
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()
    
    def drivers_network():
        color_red = colorama.Fore.RED + colorama.Style.BRIGHT
        color_cyan = colorama.Fore.CYAN + colorama.Style.BRIGHT
        color_green = colorama.Fore.GREEN + colorama.Style.BRIGHT
        color_white = colorama.Fore.WHITE + colorama.Style.BRIGHT
        color_yellow = colorama.Fore.YELLOW + colorama.Style.BRIGHT
        color_reset = colorama.Fore.RESET + colorama.Style.RESET_ALL
        
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])
        request = "apt-cache search firmware-"
        output = subprocess.check_output(request, shell=True, text=True)
        package_list = output.strip().split('\n')

        package_names = [package.split()[0] for package in package_list]
        
        def install_packages(package_names):
            try:
                install_command = f"sudo apt-get install -y {' '.join(package_names)}"
                subprocess.run(install_command, shell=True, check=True)
                
                print(color_cyan)
                print("[TorogOS; Paquete instalado correctamente]")
                
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
            except subprocess.CalledProcessError as Log:
                print(color_red)
                print("[TorogOS; Ocurrió un error durante la instalación del paquete]")
                print('- Registro de error:\n')
                print(Log)
        
        print(color_green)
        print('[TorogOS; Lista de drivers/paquetes de red disponibles para su equipo]:')
        print(color_yellow + "==============================================" + color_reset)
        print(package_names)
        print(color_yellow + "==============================================" + color_reset)
        
        print(color_cyan)
        print('¿Desea iniciar con la instalación? (s/n)')
        usr = input(str('[>>]: '))
        print("OK")
        
        if usr == 's' or usr == '':
            step_size = 1
            for i in range(0, len(package_names), step_size):
                package_chunk = package_names[i:i+step_size]
                install_packages(package_chunk)
            print(color_cyan)
            subprocess.run('sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y', shell=True, check=True)

            print(color_green)
            print('\n\n[TorogOS; Instalación finalizada]')
            
            print(color_yellow + "==============================================" + color_white)
            print("ADVERTENCIA:")
            print('- Para efectuar el funcionamiento de los drivers/paquetes que acabas de instalar debes reiniciar el equipo.\n')
            print('- Solo instalaste UNA categoría de drivers/paquetes, vuelve a ejecutar el instalador y asegúrate de instalar todas las categorías necesarias para tu equipo.')
            print(color_yellow + "==============================================" + color_reset)
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()
        else:
            print(color_red)
            print('[TorogOS; Instalación cancelada]')
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()

    def drivers_audio():
        color_red = colorama.Fore.RED + colorama.Style.BRIGHT
        color_cyan = colorama.Fore.CYAN + colorama.Style.BRIGHT
        color_green = colorama.Fore.GREEN + colorama.Style.BRIGHT
        color_white = colorama.Fore.WHITE + colorama.Style.BRIGHT
        color_yellow = colorama.Fore.YELLOW + colorama.Style.BRIGHT
        color_reset = colorama.Fore.RESET + colorama.Style.RESET_ALL
        
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])
        request = "apt-cache search alsa-"
        output = subprocess.check_output(request, shell=True, text=True)
        package_list = output.strip().split('\n')

        package_names = [package.split()[0] for package in package_list]
        
        def install_packages(package_names):
            try:
                install_command = f"sudo apt-get install -y {' '.join(package_names)}"
                subprocess.run(install_command, shell=True, check=True)
                
                print(color_cyan)
                print("[TorogOS; Paquete instalado correctamente]")
                
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
            except subprocess.CalledProcessError as Log:
                print(color_red)
                print("[TorogOS; Ocurrió un error durante la instalación del paquete]")
                print('- Registro de error:\n')
                print(Log)
        
        print(color_green)
        print('[TorogOS; Lista de drivers/paquetes de audio disponibles para su equipo]:')
        print(color_yellow + "==============================================" + color_reset)
        print(package_names)
        print(color_yellow + "==============================================" + color_reset)
        
        print(color_cyan)
        print('¿Desea iniciar con la instalación? (s/n)')
        usr = input(str('[>>]: '))
        print("OK")
        
        if usr == 's' or usr == '':
            step_size = 1
            for i in range(0, len(package_names), step_size):
                package_chunk = package_names[i:i+step_size]
                install_packages(package_chunk)
            print(color_cyan)
            subprocess.run('sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y', shell=True, check=True)

            print(color_green)
            print('\n\n[TorogOS; Instalación finalizada]')
            
            print(color_yellow + "==============================================" + color_white)
            print("ADVERTENCIA:")
            print('- Para efectuar el funcionamiento de los drivers/paquetes que acabas de instalar debes reiniciar el equipo.\n')
            print('- Solo instalaste UNA categoría de drivers/paquetes, vuelve a ejecutar el instalador y asegúrate de instalar todas las categorías necesarias para tu equipo.')
            print(color_yellow + "==============================================" + color_reset)
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()
        else:
            print(color_red)
            print('[TorogOS; Instalación cancelada]')
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()
    
    def drivers_printers():
        color_red = colorama.Fore.RED + colorama.Style.BRIGHT
        color_cyan = colorama.Fore.CYAN + colorama.Style.BRIGHT
        color_green = colorama.Fore.GREEN + colorama.Style.BRIGHT
        color_white = colorama.Fore.WHITE + colorama.Style.BRIGHT
        color_yellow = colorama.Fore.YELLOW + colorama.Style.BRIGHT
        color_reset = colorama.Fore.RESET + colorama.Style.RESET_ALL
        
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])
        request = "apt-cache search printer-driver-"
        output = subprocess.check_output(request, shell=True, text=True)
        package_list = output.strip().split('\n')

        package_names = [package.split()[0] for package in package_list]
        
        def install_packages(package_names):
            try:
                install_command = f"sudo apt-get install -y {' '.join(package_names)}"
                subprocess.run(install_command, shell=True, check=True)
                
                print(color_cyan)
                print("[TorogOS; Paquete instalado correctamente]")
                
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
            except subprocess.CalledProcessError as Log:
                print(color_red)
                print("[TorogOS; Ocurrió un error durante la instalación del paquete]")
                print('- Registro de error:\n')
                print(Log)
        
        print(color_green)
        print('[TorogOS; Lista de drivers/paquetes de impresoras disponibles para su equipo]:')
        print(color_yellow + "==============================================" + color_reset)
        print(package_names)
        print(color_yellow + "==============================================" + color_reset)
        
        print(color_cyan)
        print('¿Desea iniciar con la instalación? (s/n)')
        usr = input(str('[>>]: '))
        print("OK")
        
        if usr == 's' or usr == '':
            step_size = 1
            for i in range(0, len(package_names), step_size):
                package_chunk = package_names[i:i+step_size]
                install_packages(package_chunk)
            print(color_cyan)
            subprocess.run('sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y', shell=True, check=True)

            print(color_green)
            print('\n\n[TorogOS; Instalación finalizada]')
            
            print(color_yellow + "==============================================" + color_white)
            print("ADVERTENCIA:")
            print('- Para efectuar el funcionamiento de los drivers/paquetes que acabas de instalar debes reiniciar el equipo.\n')
            print('- Solo instalaste UNA categoría de drivers/paquetes, vuelve a ejecutar el instalador y asegúrate de instalar todas las categorías necesarias para tu equipo.')
            print(color_yellow + "==============================================" + color_reset)
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()
        else:
            print(color_red)
            print('[TorogOS; Instalación cancelada]')
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()
    
    
    """
    [Corpus; CODECS]
    """
    def codecs_multimedia():
        color_red = colorama.Fore.RED + colorama.Style.BRIGHT
        color_cyan = colorama.Fore.CYAN + colorama.Style.BRIGHT
        color_green = colorama.Fore.GREEN + colorama.Style.BRIGHT
        color_white = colorama.Fore.WHITE + colorama.Style.BRIGHT
        color_yellow = colorama.Fore.YELLOW + colorama.Style.BRIGHT
        color_reset = colorama.Fore.RESET + colorama.Style.RESET_ALL
        
        print(color_cyan)
        print("[TorogOS; Descarga e instalación de códecs multimedia para su equipo]")
        print("- ¿Desea iniciar la instalación? (s/n)")
        print(color_yellow)
        usr = input(str("[>>]: "))
        print("OK")
        print(color_reset)
        
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])
        packages = [
                'ubuntu-restricted-extras', 'libavcodec-extra', 'chromium-codecs-ffmpeg-extra', 'gstreamer1.0-plugins-bad', 'gstreamer1.0-plugins-ugly',
                'gstreamer1.0-libav', 'gstreamer1.0-alsa', 'gstreamer1.0-plugins-base', 'gstreamer1.0-plugins-good', 'gstreamer1.0-x',
                'libgstreamer1.0-0', 'gstreamer1.0-clutter-3.0', 'gstreamer1.0-omx-bellagio-config', 'gstreamer1.0-omx-generic', 'gstreamer1.0-omx-generic-config',
                'gstreamer1.0-opencv', 'gstreamer1.0-wpe', 'gstreamer1.0-gl', 'gstreamer1.0-gtk3', 'gstreamer1.0-pulseaudio',
                'gstreamer1.0-qt5', 'gstreamer1.0-pipewire', 'gstreamer1.0-adapter-pulseeffects', 'gstreamer1.0-autogain-pulseeffects', 'gstreamer1.0-convolver-pulseeffects',
                'gstreamer1.0-crystalizer-pulseeffects'
        ]
        
        def install_packages(package_names):
            try:
                install_command = f"sudo apt-get install -y {' '.join(package_names)}"
                subprocess.run(install_command, shell=True, check=True)
                
                print(color_cyan)
                print("[TorogOS; Paquete instalado correctamente]")
                
                print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
            except subprocess.CalledProcessError as Log:
                print(color_red)
                print("[TorogOS; Ocurrió un error durante la instalación del paquete]")
                print('- Registro de error:\n')
                print(Log)
        
        if usr == 's' or usr == '':
            step_size = 1
            for i in range(0, len(packages), step_size):
                package_chunk = packages[i:i+step_size]
                install_packages(package_chunk)
            subprocess.run('sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y', shell=True, check=True)
            print('\n\n')
            print(color_yellow + "==============================================" + color_green)
            print("[TorogOS; Códecs multimedia instalados]")
            print(color_yellow + "==============================================" + color_reset)
                
            print("\n\n\n" + color_white)
            input("[ Presiona cualquier tecla para cerrar esta ventana ]")
            sys.exit()
        else:
            print(color_red)
            print('[TorogOS; Instalación cancelada]')
            
            print(color_green)
            print('\n\n\n')
            input("[ Presiona cualquier tecla para cerrar esta ventana ]\n")
            sys.exit()