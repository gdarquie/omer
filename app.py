import markdown
from bs4 import BeautifulSoup
from os import walk

input_folder = './source/'
output_folder = './dist/'

# list only files in input folder (not directories) and only at top level
filenames = next(walk(input_folder), (None, None, []))[2]  # [] if no file

# create html file
project_name = "Voyage en Tchéquie"
html_template = """
<html>
    <head>
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" 
        integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
        crossorigin="anonymous">
        <link rel="stylesheet" href="./style/default.css">
    </head>
    <body class='container-fluid'>
        <div>
            <h1 class='main-title'>""" + project_name + """</h1>
            <div id='omer'></div>
        </div>
    </body>
</html>
"""


def create_html_file(filename_with_extension):
    if filename_with_extension.endswith('.md'):
        # remove extension in filename
        filename = filename_with_extension[:-3]

        # cmcreate a html file from the template
        soup = BeautifulSoup(html_template, "html.parser")

        # read the md source file
        with open(input_folder + filename_with_extension, 'r') as f:
            text = f.read()

        # we append the md content converting it into a new soup
        soup.div.append(BeautifulSoup(markdown.markdown(text), 'html.parser'))

        # create a new html file with our html template
        f = open(output_folder + filename + '.html', "w")
        f.write(str(soup))


# convert each md file into html
for filename in filenames:
    create_html_file(filename)

# create an index page
