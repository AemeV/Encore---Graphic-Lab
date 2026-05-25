import http.server, functools

handler = functools.partial(
    http.server.SimpleHTTPRequestHandler,
    directory='/Users/alejandromarin/Desktop/Encore/Iso App'
)

with http.server.HTTPServer(('', 3333), handler) as httpd:
    print('Serving Isotipo Builder at http://localhost:3333')
    httpd.serve_forever()
