#
#   This is the Robotics Language compiler
#
#   Parameters.py: Definition of the parameters for this package
#
#   Created on: 19 September, 2018
#       Author: Gabriel Lopes
#      Licence: license
#    Copyright: copyright
#
from RoboticsLanguage.Base.Types import arguments, optional, returns

language = {
    'cpp': {
        'definition': {
            'arguments': arguments('anything'),
            'returns': returns('none')
        },
    }
}