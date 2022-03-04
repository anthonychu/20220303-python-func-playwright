# Playwright in Python Azure Functions

1. Ensure `playwright` is in requirements.txt.

1. Deploy to Azure Functions v4 consumption plan using remote build (this is the default).

1. The app won't work because chromium is not installed. Add 2 app settings:
    - `PLAYWRIGHT_BROWSERS_PATH`: `/home/site/wwwroot`
        - This tells Playwright to install and use chromium from `/home/site/wwwroot`
    - `POST_BUILD_COMMAND`: `PYTHONPATH=/tmp/zipdeploy/extracted/.python_packages/lib/site-packages /tmp/oryx/platforms/python/3.9.7/bin/python3.9 -m playwright install chromium`
        - This is hacky and brittle because the Python version is bound to change. But it works for now. What this does is to run `playwright install chromium` in the Python version that was used to build the app. It'll install it to `/home/site/wwwroot` because of the previous app setting.

1. Deploy again, this time the post build command will run and hopefully it works.