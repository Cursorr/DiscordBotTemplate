## Discord Bot Template

It's a simple use library for bot discord.py developers. 

## Objective 

Sometimes, when creating a new project, the setup part took a long time. That's why `DBT` is here, to help you setup everything easily and win a lot of time.

## How to use ?

**DBT** is very very simple to use, all you need is to download the package. Then create a folder with a python script in which you have to call those 2 functions.

Make sure to download it first:

```
pip3 install git@github.com:Cursorr/DiscordBotTemplate.git
```

## Prototype

```py
from dbt import creator

setup = creator.Setup("Bot Name")
setup.start()
```

This will permit the creation of the main file, config and the cogs folder.

```
├── cogs
│   └── empty
│
├── config.json
└── botname.py
```

After this, you have also the `new_cog()` function permitting you to create a cog an example is more telling;

```py
setup.new_cog("Cogname")
setup.new_cog("Test")
```

Project files after this:

```
├── cogs
│   ├── cogname.py
│   └── test.py
│
├── config.json
└── botname.py
```

## Note

Everyone can contribute to this repository. If you have any ideas to improve it, make sure to create a pull request.