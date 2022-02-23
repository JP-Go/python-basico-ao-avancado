from string import Template
from datetime import datetime

with open('aulas/template.html', 'r') as html:
    template = Template(html.read())
    hoje = datetime.now().strftime('%d/%m/%Y')
    corpo = template.safe_substitute(nome='Luis', data=hoje)

print(corpo)
