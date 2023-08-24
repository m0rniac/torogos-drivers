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

from console import TorogOS
from PyInquirer import prompt, Separator, style_from_dict, Token

class Bar:
    @staticmethod
    def menu():
        custom_style = style_from_dict({
            Token.Separator: '#00FFFF',
            Token.QuestionMark: '#673ab7 bold',
            Token.Selected: '#cc5454',
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: '',
            Token.Answer: '#f44336 bold',
            Token.Question: '#FFD700 bold',
        })

        options = [
            {
                'type': 'list',
                'name': 'opcion',
                'message': 'Selecciona una opción:',
                'choices': [
                    Separator('Drivers:'),
                    {
                        'name': '- Gráficos (Video/Graphics)',
                        'value': TorogOS.drivers_graphics,
                    },
                    {
                        'name': '- Audio (Sound)',
                        'value': TorogOS.drivers_audio,
                    },
                    {
                        'name': '- Red (Network)',
                        'value': TorogOS.drivers_network,
                    },
                    {
                        'name': '- Impresoras (Printers)',
                        'value': TorogOS.drivers_printers
                    },
                    Separator('CODECS:'),
                    {
                        'name': '- Multimedia',
                        'value': TorogOS.codecs_multimedia,
                    }
                ],
                'style': custom_style
            }
        ]
        answers = prompt(options)
        choose = answers['opcion']

        if callable(choose):
            content = choose()
            print(content)
        else:
            print(f"Has seleccionado: {choose}")