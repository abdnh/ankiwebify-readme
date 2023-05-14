# ankiwebify-readme

An ad-hoc Python script that takes a readme file written in Markdown and converts it to an HTML file containing only tags allowed in [AnkiWeb](https://ankiweb.net/about) for the description of decks and add-ons uploaded there.

It's not perfect and you'll probably need to edit the resulting file, but it may
save you some time if you use roughly the same description for your Anki add-ons uploaded to AnkiWeb
as the GitHub repository's README.md, and used to manually convert your README.md to the HTML allowed by AnkiWeb.

## Usage

```
usage: ankiwebify.py [-h] [--github NAME] [--branch BRANCH] file

Take a Markdown file and output an AnkiWeb HTML file

positional arguments:
  file             markdown file to convert

optional arguments:
  -h, --help       show this help message and exit
  --github NAME    GitHub repo name to convert relative links according to
  --branch BRANCH  GitHub repo branch to use for relative links
```

## Related

I also published another implementation of this as an extension for VS Code. You might want to check that too since it's probably easier to use if you're a VS Code user: https://github.com/abdnh/vscode-ankiwebify
