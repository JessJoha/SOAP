from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, a, b):
        return a - b

application = Application(
    [CalculatorService],
    tns='calculator.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_app)
    print("Servidor SOAP corriendo en http://127.0.0.1:8000")
    server.serve_forever()
