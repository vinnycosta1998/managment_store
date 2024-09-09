import requests

class CEP:
    def __init__(self, cep):
        self.char = ""
        self.cep = cep
        self.validate_cep()

    def validate_cep(self):
        self.cep = self.cep.replace(".", "").replace("-", "")
        self.list_cep = list(self.cep)
        print(len(self.list_cep))
        assert len(self.list_cep) != 8, "CEP inválido"
        try:
            for i in range(0, len(self.list_cep)):
                self.list_cep[i] = int(self.list_cep[i])
            
            for j in self.list_cep:
                self.char += str(j)

            self.cep = self.char
            self.search_cep()
        except ValueError:
            print("CEP invalido")

    def search_cep(self):
        response = requests.get(f"viacep.com.br/ws/${self.cep}/json/")
        print(response.json)

cep = str(input("Digite um cep"))

CEP(cep)