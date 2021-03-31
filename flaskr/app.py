from config import *
from models import Historico
from client import *
import pytz
from datetime import datetime


@app.route("/listar_historico")
def listar_historico():
    historicos = db.session.query(Historico).all()
    retorno = []
    for p in historicos:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


def adicionar_historico(historico):
    db.session.add(historico)
    db.session.commit()


@app.route("/cidade/<nome_cidade>", methods=["GET"])
def buscar_tempo_cidade(nome_cidade):
    try:
        dicionario = parse_to_historico(
            mgr.weather_at_place(nome_cidade))

        historico = Historico.parse_dict_to_historico(dicionario)
        adicionar_historico(historico)

        return dicionario
    except TimeoutError:
        return "A Weather API demorou demais para responder. Tente novamente."


def parse_to_historico(observation):

    timezone = pytz.timezone("America/Sao_Paulo")
    temperatura = observation.weather.temperature(unit="celsius")
    vento = observation.weather.wind(unit="km_hour").get("speed")
    data_referencia = observation.weather.reference_time(
        timeformat="date").astimezone(timezone)
    data_consulta = datetime.now().astimezone(timezone)

    return {
        "nome_da_cidade": observation.location.name,
        "sigla_do_pais": observation.location.country,
        "sensacao_termica": temperatura.get("feels_like"),
        "temperatura": temperatura.get("temp"),
        "temperatura_maxima": temperatura.get("temp_max"),
        "temperatura_minima": temperatura.get("temp_min"),
        "umidade": observation.weather.humidity,
        "status": observation.weather.detailed_status,
        "vento": vento,
        "data_hora_referencia": data_referencia,
        "data_hora_consulta": data_consulta
    }


if __name__ == "__main__":
    app.run(debug=True)
