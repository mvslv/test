name = input("твое имя беженец?")
age = input("сколько тебе лет?")
print("привет," + name + "!")
print("тебе" + age + " лет, это пиздец, старик. мне жаль тебя")


from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('8183c65ce9ea655ff0958636bfd8eb5f', config_dict )
mgr = owm.weather_manager()

place = input("давай я тебе дам совет! в каком городе ты оказался?")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"] 
print ("в городе  "   +  place  +    "  сейчас  "    +  w.detailed_status)
print("температура на улице, в данный момент где-то " + str(temp))

if temp < 10:
    print("на улице холодрыга сиди дома, или оденься как Чукча")
elif temp < 20:
    print("погода нормас иди гуляй, но надень шапку")
else:
    print("температура огонь! одевай ... в принципе можешь даже в трусах идти")
input()
