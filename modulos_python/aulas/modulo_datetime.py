from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays  # type: ignore

# formato: datetime(ano,mes,dia[,hora,minuto,segundo])
data = datetime(2019, 4, 20)
print(data)
# datetime().strftime("fmt_string"hora_str) -> ret string formatada a partir da data
print(data.strftime("%d/%m/%Y"))
# datetime.strptime("data_str","format") -> ret um obj. datetime a partir de uma string
print(datetime.strptime("22/08/1998", '%d/%m/%Y'))
# datetime().timestamp() -> ret o timestamp da data compativel com POSIX
# (segundos desde 1/1/1970 até a data que o objeto representa)
# fromtimestamp() faz o processo contrário
print(data.timestamp())

# timedelta representa o intervalo entre duas datas
# timedelta(days=5) representa o intervalo de 5 dias entre duas datas
# pode-se somar objetos timedelta a objetos datetime para representar
# a passagem de tempo
acrescimo_14dias = timedelta(weeks=2)  # adiciona 14 dias
acrescimo_um_mes = timedelta(days=30)

nova_data = data + acrescimo_14dias
nova_data_apos_mes = data + acrescimo_um_mes
print(nova_data)
print(nova_data - data)

print(nova_data_apos_mes)
print(nova_data_apos_mes - data)

# timedelta possui os atributos/métodos:
#   -> seconds: porção do intervalo em segundos
#   -> total_seconds: intervalo de tempo total em segundos
#   -> days: porção do intervalo em dias
#   -> total_days: porção do intervalo em dias

## Como formatar em portugues?

# setlocale(category [,locale_str]): define a localização para o ambiente
# passar locale_str se quiser forçaar um locale específico
# LC_ALL: significa todas as variáveis de localização
setlocale(LC_ALL, '')
dt = datetime.now()
data_formatada = dt.strftime("%A, %d de %B de %Y")
print(data_formatada)

# Como conseguir o ultimo dia do mes
mes_atual = dt.month
ultimo_dia_do_mes = mdays[mes_atual]
print(ultimo_dia_do_mes)
