### Testing grammarly with selenium

[![Run
it](https://github.com/zodman/test-grammarly/actions/workflows/run.yml/badge.svg)](https://github.com/zodman/test-grammarly/actions/workflows/run.yml)

Html report like artifact on the [github actions](https://github.com/zodman/test-grammarly/actions/workflows/run.yml)....

** Note: Only behind docker selenium/standalone-chrome can check if extension is installed because of [Problems founded](https://github.com/zodman/test-grammarly#problems-founded)


# For run

```bash
python3.8 -m venv .env
source .env/bin/activate # or .env/Scripts/activate on win
pip install -r requirements.txt 
pytest --grammarly-ext utils/grammarly.14.1006.0.crx # for run with grammarly installed
# or
pytest -k no_installed # for run without grammarly installed
```

## [Test Plan](https://github.com/zodman/test-grammarly/search?l=gherkin)


### How detect if grammarly chrome extension is installed ?

I had to go to the extension directory:

on windows:

    f"/mnt/c/Users/{user}/AppData/Local/Google/Chrome/User Data/{profile_name}/Extensions/{extension_id}"
    
Then i had to inspect the definition extension of the grammarly `manifest.json`

Find files loaded at start. Then inspect that js..

I discover `src/js/Grammarly-check.js` that's mean: _"OK if check maybe there is the definition of loaded or installed"_

With `js-beautify` unminificate the code and inspect the functions and found:

![](https://i.imgur.com/5JGyUJv.png)

When the plugin is loaded there are some `data-` properties  attached to the `<body>` tag.

*PUM! Grammarly detected ...*

### Problems founded

* When you run on docker-selenium webdriver=remote, the application upload the file crx, then 
  selenium cann't handle it and raise a java heap memory exception.. I don't fix it
  because are out scope of the project.
