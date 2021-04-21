### Testing grammarly with selenium


# For run

```bash
python -m venv .env
source .env/bin/activate
pytest --grammarly-ext utils/grammarly.14.1006.0.crx # for run with grammarly installed
# or
pytest # for run without grammarly installed
```


### How detect if grammarly chrome extension is installed ?

I had to go to the extension directory:

on windows:

    f"/mnt/c/Users/{user}/AppData/Local/Google/Chrome/User Data/{profile_name}/Extensions/{extension_id}"
    
on my machine:
/mnt/c/Users/QA/AppData/Local/Google/Chrome/User Data/Profile 1/Extensions/kbfnbcaeplbcioakkpcpgfkobkghlhen

Then i had to inspect the definition extension of the grammarly `manifest.json`

And search all files load when the extension are loaded. To inspect that js..

I discover `src/js/Grammarly-check.js` that's mean ok if check maybe there is the definition of loaded or installed

With `js-beautify` unminificate the code and inspect the functions and found:

![](https://i.imgur.com/5JGyUJv.png)

When the plugin is loaded there are some `data-` properties  attached to the `<body>` tag.


PUM! Grammarly detected ...

### Problems founded

* When you run on docker-selenium, the application upload the file crx, then 
  selenium can handle and raise a java heap memory exception.. I don't fix it
  because are out scope of this.
