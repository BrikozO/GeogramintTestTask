import os
import shutil

from CLI import geogramint_cli

if __name__ == "__main__":
    shutil.rmtree("cache_telegram", ignore_errors=True)
    shutil.rmtree("cache", ignore_errors=True)
    geogramint_cli.CLI()
    shutil.rmtree("cache", ignore_errors=True)
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log")
    print()
