#coding=utf8


# this module replace all my tags to html tags


import os
from settings import PROJECT_PATH


def replacer():
    image = """
<table class='note'>
    <tr>
        <td>
            <img src='/statics/images/pic.png' width='40' height='40' />
        </td>
        <td valign='middle' width='95%'><h4>
"""
    image2 = "</h4></td></tr><tr><td colspan='2'>"
    image3 = "</td></tr></table>"

    note = """
<table class='note'>
    <tr>
        <td valign='top'>
            <img src='/statics/images/note.png' width='40' height='35' />
        </td>
        <td width='95%'><h4>
"""
    note2 = "</h4>"
    note3 = "</td></tr></table>"

    jadval = """
<table class='note'>
    <tr>
        <td>
            <img src='/statics/images/table.png' width='45' height='40' />
        </td>
        <td valign='middle' width='95%'><h4>"""
    jadval2 = "</h4></td></tr><tr><td colspan='2'><table class='puzzle'>"
    jadval3 = "</table></td></tr></table>"

    python_code = '<pre class="brush: py">'
    html_code = '<pre class="brush: html">'
    sql_code = '<pre class="brush: sql">'
    bash_code = '<pre class="brush: bash">'
    end_code = '</pre>'

    book_path = "%s/../templates/djangobook/" % (PROJECT_PATH)
    include_path = "%s/../templates/includes/" % (PROJECT_PATH)

    for path in os.listdir(book_path):
        if path[0] != ".":
            fread = open("%s%s" % (book_path, path), "r")

            if not os.path.exists(include_path):
                os.mkdir(include_path)

            fwrite = open("%s%s.html" % (include_path, path), "w")
            matn = fread.read()

            matn = matn.replace("<", "&lt;")
            matn = matn.replace(">", "&gt;")
            matn = matn.replace("{", "&#123;")
            matn = matn.replace("}", "&#125;")

            matn = matn.replace("[br]", "<br />")

            matn = matn.replace("[hr]", "<hr ")
            matn = matn.replace("[hr/]", ">")

            matn = matn.replace("[img]", "<img ")
            matn = matn.replace("[img/]", ">")
            matn = matn.replace("[/img]", "</img>")

            matn = matn.replace("[p]", "<p ")
            matn = matn.replace("[p/]", ">")
            matn = matn.replace("[/p]", "</p>")

            matn = matn.replace("[button]", "<button ")
            matn = matn.replace("[button/]", ">")
            matn = matn.replace("[/button]", "</button>")

            matn = matn.replace("[h2]", "<h2 ")
            matn = matn.replace("«هد/»", ">")
            matn = matn.replace("[/h2]", "</h2>")

            matn = matn.replace("[h3]", "<h3 ")
            matn = matn.replace("«هس/»", ">")
            matn = matn.replace("[/h3]", "</h3>")

            matn = matn.replace("[h4]", "<h4 ")
            matn = matn.replace("[h4/]", ">")
            matn = matn.replace("[/h4]", "</h4>")

            matn = matn.replace("[h5]", "<h5 ")
            matn = matn.replace("[h5/]", ">")
            matn = matn.replace("[/h5]", "</h5>")


            matn = matn.replace("[ul]", "<ul ")
            matn = matn.replace("[ul/]", ">")
            matn = matn.replace("[/ul]", "</ul>")

            matn = matn.replace("[ol]", "<ol ")
            matn = matn.replace("[ol/]", ">")
            matn = matn.replace("[/ol]", "</ol>")

            matn = matn.replace("[li]", "<li ")
            matn = matn.replace("[li/]", ">")
            matn = matn.replace("[/li]", "</li>")

            matn = matn.replace("[tr]", "<tr ")
            matn = matn.replace("[tr/]", ">")
            matn = matn.replace("[/tr]", "</tr>")

            matn = matn.replace("[th]", "<th ")
            matn = matn.replace("[th/]", ">")
            matn = matn.replace("[/th]", "</th>")

            matn = matn.replace("[td]", "<td ")
            matn = matn.replace("[td/]", ">")
            matn = matn.replace("[/td]", "</td>")

            matn = matn.replace("[table]", "<table ")
            matn = matn.replace("[table/]", ">")
            matn = matn.replace("[/table]", "</table>")

            matn = matn.replace("[چپ]", "<span dir='ltr'>")
            matn = matn.replace("[/چپ]", "</span>")

            matn = matn.replace("[a]", "<a ")
            matn = matn.replace("[a/]", ">")
            matn = matn.replace("[/a]", "</a>")

            matn = matn.replace("[pre]", "<pre" )
            matn = matn.replace("[pre/]", ">")
            matn = matn.replace("[/pre]", "</pre>")

            matn = matn.replace("[code]", python_code)
            matn = matn.replace("[code python]", python_code)
            matn = matn.replace("[code py]", python_code)
            matn = matn.replace("[code html]", html_code)
            matn = matn.replace("[code sql]", sql_code)
            matn = matn.replace("[code bash]", bash_code)
            matn = matn.replace("[/code]", end_code)

            matn = matn.replace("[note]", note)
            matn = matn.replace("[note/]", note2)
            matn = matn.replace("[/note]", note3)

            matn = matn.replace("[image]", image)
            matn = matn.replace("[image/]", image2)
            matn = matn.replace("[/image]", image3)

            matn = matn.replace("[puzzle]", jadval)
            matn = matn.replace("[puzzle/]", jadval2)
            matn = matn.replace("[/puzzle]", jadval3)

            fwrite.write(matn)
            fread.close()
            fwrite.close()

            print "%s Done!" % path

if __name__ == "__main__":
    replacer()
