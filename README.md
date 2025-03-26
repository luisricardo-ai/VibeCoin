# 🎧💰 VibeCoin
VibeCoin is a data engineering project that explores the correlation between Spotify’s Top 50 Global songs and Bitcoin price fluctuations. By analyzing music sentiment and market trends, it aims to uncover potential connections between global vibes and crypto volatility.

## Prerequisites
To run VibeCoin, ensure you have the following installed:

* [Pyenv](https://github.com/pyenv/pyenv)
* [Poetry](https://python-poetry.org)

## Installation
1. Clone 
```sh
   git clone https://github.com/luisricardo-ai/VibeCoin.git
```

2. Use the right version of Python for this project
```sh
    pyenv install 3.13.2
    pyenv local 3.13.2
```

3. Virtual Enviroment
```sh
    poetry env use $(pyenv which python)
    poetry env activate
```

4. Install dependencies
```sh
    poetry install
```

## How to run the code?
At this project i used [taskipy](https://github.com/taskipy/taskipy), so you can use the command *task* with some few other options. If you would like to check what those commands run behind the scenes, go to the *pyproject.toml* file at the section **[tool.taskipy.tasks]**

1. Run unit tests.
```sh
    task test
```

2. Run the entire pipeline
```sh
    task run
```

## Contact
* Luis Palharini - palharini.luis@gmail.com