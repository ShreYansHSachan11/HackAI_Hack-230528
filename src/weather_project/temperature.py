from uagents import Agent, Bureau, Context, Model
import requests
import os
class Message(Model):
    message: str

temp = Agent(name="temp", seed = "temp recovery phrase")
alert = Agent(name="alert", seed="temperature range")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api = "86a901043ff6b04e249a9dc5d84bc2ad"

@temp.on_event("startup")
async def reset_count(ctx: Context):
    ctx.storage.set("count", 0)

city = os.environ.get('LOCATION', 'delhi')
min_temp = int(os.environ.get('MIN_TEMP', '0'))
max_temp = int(os.environ.get('MAX_TEMP', '0'))


# class TemperaturePreferences(Model):
#     min_temp: float
#     max_temp: float
#     temp_kelvin: float

@temp.on_interval(period=5.0)
async def temperature(ctx: Context):
    url = base_url + "appid=" + api + "&q=" + city
    response = requests.get(url).json()
    try:
     temp_kelvin = response['main']['temp']
    except KeyError:
     print("Key 'main' or 'temp' not found in JSON response.")

    if (temp_kelvin > min_temp and temp_kelvin < max_temp):
        ctx.storage.set("count", 0)
    if (temp_kelvin < min_temp and ctx.storage.get("count") != 1):
            await ctx.send(alert.address, Message(message = temp_kelvin))
            ctx.storage.set("count", 1)
    if (temp_kelvin > max_temp and ctx.storage.get("count") != 2):
        await ctx.send(alert.address, Message(message = temp_kelvin))
        ctx.storage.set("count", 2)

@alert.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    str_get_temp= msg.message
    get_temp = float(str_get_temp) -273

    if get_temp < min_temp:
        ctx.logger.info(f"Current Temperature is below {min_temp}")
        message = f"Current Temperature is below {min_temp}"
        ctx.storage.set("message", message)
    elif get_temp > max_temp:
        message = f"Current Temperature is above {max_temp}"
        ctx.storage.set("message", message)
        ctx.logger.info(f"Current Temperature is above {max_temp}")

bureau = Bureau()
bureau.add(temp)
bureau.add(alert)
bureau.run()