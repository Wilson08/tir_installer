from __future__ import print_function, unicode_literals
import os
from PyInquirer import style_from_dict, Token, prompt, Separator
import subprocess

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


questions = [
    {
        'type': 'checkbox',
        'message': 'Select toppings',
        'name': 'toppings',
        'choices': [
            Separator('= Select installing ='),
            {
                'name': '*Required* Python',
                'checked': True
            },
            {
                'name': 'Required*  GIT',
                'checked': True
            },
            {
                'name': 'Mozilla Firefox'
            },

        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
if(("Python" in answers['toppings'][0])and ("GIT" in answers['toppings'][1])):
    os.system("%cd%\install_chocolatey.cmd")
    os.system("%cd%\install_package.cmd")
    os.system("pause")