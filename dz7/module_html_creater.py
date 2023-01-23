import module_file_editing as file

def create(data):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    for item in data:
        html += '    <p {}> {}  {}</p>\n'\
            .format(style, item[0], item[1])
    html += '  </body>\n</html>'
    
    file.file_write('index.html',html)

def create_full(data):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    for item in data:
        item = item.split(',')
        html += '<p {}>{}   {}    {}    {}    {}</p>\n'\
        .format(style, item[0], item[1] ,item[2],item[3],item[4])
    html += '  </body>\n</html>'
    
    file.file_write('index.html',html)