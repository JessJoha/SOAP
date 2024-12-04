from zeep import Client

# Conecta al servidor SOAP
client = Client('http://127.0.0.1:8000/?wsdl')

# Realiza operaciones
print("Sumando 10 + 5:", client.service.add(10, 5))
print("Restando 10 - 5:", client.service.subtract(10, 5))
