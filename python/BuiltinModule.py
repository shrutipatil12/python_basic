#Program to find the available built-in modules.

import sys
import textwrap
module_name = ', '.join(sys.builtin_module_names)
print(textwrap.fill(module_name))

