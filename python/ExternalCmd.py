#Program to call an external command in program.

import os
from subprocess import call
call(["man","ls"])