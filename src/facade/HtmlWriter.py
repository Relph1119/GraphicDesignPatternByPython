class HtmlWriter:
    def __init__(self, file):
        self.file = file

    def title(self, title):
        self.file.write("<html>")
        self.file.write("<head>")
        self.file.write("<title>" + title + "</title>")
        self.file.write("</head>")
        self.file.write("<body>\n")
        self.file.write("<h1>" + title + "</h1>\n")

    def paragraph(self, msg):
        self.file.write("<p>" + msg + "</p>")
    
    def link(self, href, caption):
        self.paragraph("<a href=\"" + href + "\">" + caption + "</a>")
    
    def mailto(self, mailaddr, username):
        self.link("mailto:" + mailaddr, username)

    def close(self):
        self.file.write("</body>")
        self.file.write("</html>\n")
        self.file.close()