# Plugin docs

These docs follow the format of the plugin located at ../addons/blah.py

---

## The Basics

When making a plugin, a few things are necessary at first:

### 1. Headers

Gotta import the headers!

```py
import discord
from discord.ext import commands
from sys import argv
```

### 2. Define a class

Define a class that will contain your code and preferably a description.

I also added an __init__ function that imports bot from the main script and prints a statement saying that the plugin has been loaded. You can customize this if you want.

```py
class Things:
    """
    Random things.
    """
    def __init__(self, bot):
          self.bot = bot
          print('Addon "{}" loaded'.format(self.__class__.__name__))
```

Then, put whatever code you want in there! More on that later.

### 3. Set up your bot!

After all your code, add this statement at the end to wrap things up:

```py
import discord
from discord.ext import commands
from sys import argv

class Things:
    """
    Random things.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    # Your commands go here

def setup(bot):
    bot.add_cog(Things(bot))
```

---

## Scripting Commands

This bot uses the commands framework from discord.py. The documentation on that is located [here](). This bit will walk you through making a basic function.

First, you must declare that the following function is a command the bot will use. (i.e. `def foo(self)` in code == `!foo` in in chat.) This can be done by adding a commands decorator.

```py
@commands.command()
```

Then, define your function as an asynchronous function, and preferably add a description so we know what it's doing:

```py
async def ping(self):
    """About the bot"""
```

Lastly, define your code! Read the discord.py docs to learn more about what you can do with your commands and script it up! Below we just await the bot sending a message, and then the command ends.

```py
@commands.command()
async def ping(self):
    """About the bot"""
    await self.bot.say("pong!")
```
