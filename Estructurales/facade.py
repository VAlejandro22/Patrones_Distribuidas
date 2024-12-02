#FACADE (FACHADA)
class SMTPServer:
    def connect(self):
        return "Conectado al servidor SMTP"

    def send(self, message):
        return f"Enviado: {message}"

class Logger:
    def log(self, message):
        print(f"Log: {message}")

class MailFacade:
    def __init__(self):
        self.server = SMTPServer()
        self.logger = Logger()

    def send_email(self, message):
        connection_result = self.server.connect()
        self.logger.log(connection_result)
        send_result = self.server.send(message)
        self.logger.log(send_result)
        return "Proceso de email completado"


# Uso FACADE
facade = MailFacade()
print(facade.send_email("Hello, World!"))