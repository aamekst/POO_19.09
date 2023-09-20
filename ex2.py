class Paciente:
    def __init__(self,nome,cpf, idade):
        self.nome=nome
        self.cpf=cpf
        self.idade=idade


class Exame:
    def __init__ (self,medico,paciente,descricao,resultado):
        self.medico=medico
        self.paciente=paciente
        self.descricao=descricao
        self.resultado=resultado

    def imprimir_exame(self):
        print(self.paciente.nome)
        print(self.paciente.cpf)
        print(self.paciente.idade)
        print('-----------------------')
        print(self.medico.nome)
        print(self.medico.crm)
        print(self.medico.especializacao)


class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome=nome
        self.crm=crm
        self.especializacao=especializacao      

paciente1 = Paciente('Marcelo Silva', '033444555-22', 26)
medico1 = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame = Exame(medico1, paciente1, 'COVID-19', 'Negativo')  
exame.imprimir_exame()	