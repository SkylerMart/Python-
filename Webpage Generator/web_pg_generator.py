f = open("webpggen.html", "x")

file = open("webpggen.html", 'a')
file.write("<html> \n<body> \nStay tuned for our amazing summer sale! \n</body> \n</html>")
file.close()

webopen = open("webpggen.html", "r")
print(webopen.read())
