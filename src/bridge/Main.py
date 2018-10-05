from Display import Display
from StringDisplayImpl import StringDisplayImpl
from CountDisplay import CountDisplay

d1 = Display(StringDisplayImpl("Hello, China."))
d2 = CountDisplay(StringDisplayImpl("Hello, World."))
d3 = CountDisplay(StringDisplayImpl("Hello, Universe."))

d1.display()
d2.display()
d3.display()
d3.multi_display(5)