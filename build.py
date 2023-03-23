import os

only_html = ""

with open("src/index.html", "r+") as html:

    for line in html.readlines():

        only_html += line

        if line == "</html>\n":

            break

    html.seek(0)
    html.truncate()
    html.seek(0)

    html.write(only_html)

    with open("src/style.css", "r") as css:

        html.seek(0, os.SEEK_END)
        html.write(f"\n\n<style>\n\n{css.read()}\n\n</style>")

    with open("src/index.js", "r") as js:

        html.seek(0, os.SEEK_END)
        html.write(f"\n\n<script>\n\n{js.read()}\n\n</script>")

os.system(f"cd \"{os.getcwd()}\" && cargo build && cargo run")