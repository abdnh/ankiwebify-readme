import re

from markdown import markdown
from bs4 import BeautifulSoup

allowed_tags = ["img", "a", "b", "i", "code", "ul", "ol", "li", "div"]


def is_relative_link(url: str) -> bool:
    return not (url.startswith("http://") or url.startswith("https://") or url.startswith("mailto:"))


def ankiwebify(filename: str, github_repo: str, branch: str = "master"):
    with open(filename, "r", encoding="utf-8") as f:
        html = markdown(f.read(), output_format="html")
    doc = BeautifulSoup(html, "html.parser")
    # add the "markdown" attribute so that markdown inside html tags in the original text is parsed
    for node in doc():
        node["markdown"] = "1"
    # reparse markdown again
    html = markdown(doc.decode(False), output_format="html5", extensions=["md_in_html"])
    # strip markdown attribute
    html = html.replace(' markdown="1"', "")
    doc = BeautifulSoup(html, "html.parser")

    for tag in doc("p"):
        for child in tag.children:
            if child.string:
                child.string.replace_with(child.string.replace("\n", " "))
            if child.name == "br":
                child.replace_with("\n")

    for tag in doc(re.compile("(ul)|(ol)")):
        for child in tag.children:
            if child.string:
                child.string.replace_with(str(child.string).replace("\n", ""))

    for tag in doc(re.compile("h1|h2|h3|h4|h5|h6")):
        tag.name = "b"
        tag.insert_before("\n")

    for tag in doc("em"):
        tag.name = "i"

    for tag in doc("strong"):
        tag.name = "b"

    if github_repo:
        for tag in doc(re.compile("(img)|(video)")):
            src = tag["src"]
            if is_relative_link(src):
                tag[
                    "src"
                ] = f"https://raw.githubusercontent.com/{github_repo}/{branch}/{src}"
        for tag in doc("a"):
            href = tag["href"]
            if is_relative_link(href):
                tag["href"] = f"https://github.com/{github_repo}/blob/{branch}/{href}"

    for tag in doc():
        if tag.name not in allowed_tags:
            tag.unwrap()

    html = doc.decode(False)

    return html


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Take a markdown file and output an AnkiWeb HTML file"
    )
    parser.add_argument("file", help="markdown file to convert")
    parser.add_argument(
        "--github",
        help="GitHub repo name to convert relative links according to",
        metavar="NAME",
    )
    parser.add_argument(
        "--branch",
        help="GitHub repo branch to use for relative links",
        default="master",
    )
    args = parser.parse_args()
    print(ankiwebify(args.file, args.github, args.branch))
