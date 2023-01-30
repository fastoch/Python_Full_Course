# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

# this file is my main program. I'll import modules into it.

import messages as msg

msg.hello()
msg.bye()

# alt
from messages import hello,bye

hello()
bye()

# display all python modules available
help("modules")

# you can also get more info here: https://docs.python.org/3/