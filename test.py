name = input("Как Вас зовут?")

print("привет," + name + "у Вас очень красивое имя!")



from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('8183c65ce9ea655ff0958636bfd8eb5f', config_dict )
mgr = owm.weather_manager()

place = input("в каком городе Вы находитесь?")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"] 
print ("в городе  "   +  place  +    "  сейчас  "    +  w.detailed_status)
print("температура на улице, в данный момент где-то " + str(temp))

if temp < 10:
    print("на улице довольно холодно. оденьтесь потеплее, и не забудьте надеть термобелье под основной одеждой. Держите ноги в тепле, выберите обувь соответсвующим температурным режимом ")
elif temp < 20:
    print("погода хорошая, можно выйти в свитере")
else:
    print("температура на улице огонь) рекомендую взять собой купальник")
input()
