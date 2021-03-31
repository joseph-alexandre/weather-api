from config import *


class Historico (db.Model):
    __tablename__ = 'historico'
    id = Column(Integer, primary_key=True)
    nome_da_cidade = Column(String(50))
    sigla_do_pais = Column(String(2))
    sensacao_termica = Column(Float(asdecimal=True))
    temperatura = Column(Float())
    temperatura_maxima = Column(Float())
    temperatura_minima = Column(Float())
    umidade = Column(Float())
    status = Column(String(30))
    vento = Column(Float(asdecimal=True, decimal_return_scale=2))
    data_hora_referencia = Column(DateTime(timezone=True))
    data_hora_consulta = Column(DateTime(timezone=True))

    def __str__(self):
        return str(self.id) + ", " + self.cidade_pesquisada

    def json(self):

        return {
            "nome_da_cidade": self.nome_da_cidade,
            "sigla_do_pais": self.sigla_do_pais,
            "sensacao_termica": str(self.sensacao_termica),
            "temperatura": str(self.temperatura),
            "temperatura_maxima": str(self.temperatura_maxima),
            "temperatura_minima": str(self.temperatura_minima),
            "umidade": self.umidade,
            "status": self.status,
            "vento": '{0:.3g}'.format(self.vento),
            "data_hora_referencia": self.data_hora_referencia,
            "data_hora_consulta": self.data_hora_consulta
        }

    def __init__(self, nome_cidade, sigla_do_pais, sensacao_termica, temperatura, temperatura_maxima, temperatura_minima, umidade, status, vento, data_hora_referencia, data_hora_consulta):
        self.nome_da_cidade = nome_cidade
        self.sigla_do_pais = sigla_do_pais
        self.sensacao_termica = sensacao_termica
        self.temperatura = temperatura
        self.temperatura_maxima = temperatura_maxima
        self.temperatura_minima = temperatura_minima
        self.umidade = umidade
        self.status = status
        self.vento = vento
        self.data_hora_referencia = data_hora_referencia
        self.data_hora_consulta = data_hora_consulta

    def parse_dict_to_historico(dictionary):
        return Historico(dictionary.get("nome_da_cidade"),
                         dictionary.get("sigla_do_pais"), dictionary.get(
                             "sensacao_termica"),
                         dictionary.get("temperatura"), dictionary.get(
                             "temperatura_maxima"),
                         dictionary.get(
                             "temperatura_minima"), dictionary.get("umidade"),
                         dictionary.get("status"), dictionary.get(
                             "vento"), dictionary.get("data_hora_referencia"),
                         dictionary.get("data_hora_consulta"))


db.drop_all()
db.create_all()
