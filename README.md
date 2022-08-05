# link-checker
Provide a URL and this script will check all the links on that page. If any are broken, it will report them after the script finishes running.

## Requirements:
```pip3 install beautifulsoup4```

```pip3 install requests```

## How to use
Save link-checker.py in a directory you can get to in the Terminal. 
Run ```python3 link-checker.py```
It will ask you to "Enter a URL:"

Paste or type in the URL you want to check for broken links. Example:
```zsh
user@scripts % python3 link-checker.py
### Check a page's links for 404 errors ###


Enter the URL:

https://notdefined.tech
```

## Example Output
```shell
...

https://notdefined.tech/blog/running-multiple-django-projects-at-once-specifying-the-ports-for-dev/
Status: 200

https://notdefined.tech
Status: 200

### No Broken Links on Page! ###

        *       *       *
```

```shell
...

https://some-example.com
Status: 200

### Broken Links Found: ###
https://some-example.com/does-not-exist.html

        *       *       *
```
