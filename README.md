# A simple tool for compiling travl markdown project into html

After writing your travel story in travl markdonw format, omer converts your travl md in html, generating a simple eco-friendly static website.

## How to use

Create a source folder in travl format: a source folder with markdown and an /img folder

Build the project:

```
bash ./shell/build.sh
```

It creates a dist/ folder with resized images and md converted in html.
It supports .png and .jpg.

Publish it with surge:

```
surge --domain my-example-domain.surge.sh
```

## About travl format

A folder named "source".

source is mandatory.

An example of a source structure:
- img (folder) mandatory
- my-text.md (markdown file)
- my-another.md (markdown file)

"img" folder can have subfolders.
You can create as many md file you need.