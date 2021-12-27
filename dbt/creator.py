import os
import json
import dbttemplates

class Setup:

    templates_path = os.path.abspath(dbttemplates.__file__).strip("\__init__.py")

    def __init__(self, name, prefix=None, color=None, token=None):
        self.name = name
        self.prefix = prefix
        self.color = color
        self.token = token


    def start(self):
        """
        Replacing variables in template file with given one, and setup the project. 
        """

        bot_file = open(f"{self.templates_path}\\bot.py", "r", encoding="utf-8")
        code = bot_file.read().replace("BotName", self.name)

        config = {
            "name": "BotName",
            "token": "token here",
            "prefix": "!",
            "color": "0xffffff"
        }

        # Replacing values in config file if exists otherwise it keeps default config.
        for item in vars(self).items():
            key, value = item
            if value:
                config[key] = value

        # Creating cogs folder.        
        os.mkdir("cogs")

        # Creating main file.
        main_file = open(self.name.replace(" ", "").lower() + ".py", "w", encoding="utf-8")
        main_file.write(code)
        main_file.close()

        # Creating config file.
        json.dump(config, open(f"config.json", "w", encoding="utf-8"), indent=4)

    def new_cog(self, name):
        name = name.lower()

        # Checking if file already exists to not crush the file and its content.
        if name + ".py" in [file.lower() for file in os.listdir("cogs")]:
            return print(f"{name}.py already exists.")

        # Replacing variables
        cog = open(f"{self.templates_path}\\cog.py", "r", encoding="utf-8")
        cog_code = cog.read().replace("CogName", name.capitalize())

        # Creating cogs folder if not exist
        if "cogs" not in os.listdir():
            os.mkdir("cogs")

        # Creation Cog File
        cog_file = open(f"cogs/{name.replace(' ', '')}.py", "w", encoding="utf-8")
        cog_file.write(cog_code)
        cog_file.close()
