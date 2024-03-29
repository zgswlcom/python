from wsgiref.simple_server import make_server

def f1():
    f1=open("index1.html","rb")
    data1=f1.read()
    return [data1]

def f2():
    f2=open("index2.html","rb")
    data2=f2.read()
    return [data2]

def application(environ, start_response):

    print(environ['PATH_INFO'])
    path=environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])


    if path=="/yuan":
        return f1()

    elif path=="/alex":
        return f2()

    else:
        return ["<h1>404</h1>".encode("utf8")]


httpd = make_server('localhost', 8502, application)

print('Serving HTTP on port 8084...')

# 开始监听HTTP请求:
httpd.serve_forever()
