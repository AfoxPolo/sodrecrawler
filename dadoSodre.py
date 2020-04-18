import requests
from bs4 import BeautifulSoup
import webbrowser

"""fechamento"""
af = '\033[m'

"""vermelho"""
a31 = '\033[1;31m'

"""verde"""
a32 = '\033[1;32m'

"""amarelo"""
a33 = '\033[1;33m'

"""azul"""
a34 = '\033[1;34m'

"""blold"""
abl = '\033[1m'


def leitor_pagina():
    ndp = 0
    pagina1 = ''
    while True:
        ndp += 1
        link_leitor = f'https://www.sodresantoro.com.br/veiculos/ordenacao/data_leilao/tipo-ordenacao/crescente/qtde' \
                      f'-itens/15/visualizacao/visual_imagem/item-atual/1/pagina/{ndp}/'
        req_leitor = requests.get(link_leitor).text
        soup = BeautifulSoup(req_leitor, 'html.parser')
        if ndp == 1:
            pagina1 = soup.findAll("h2", {"class": "titulo_1"})
        else:
            outrapagina = soup.findAll("h2", {"class": "titulo_1"})
            if pagina1 == outrapagina:
                return ndp


def pagina(retorno=False):
    link_paginas = f'https://www.sodresantoro.com.br/veiculos/ordenacao/data_leilao/tipo-ordenacao/crescente/qtde-it' \
                   f'ens/15/visualizacao/visual_imagem/item-atual/1/pagina/{pg}/'
    r = requests.get(link_paginas).text
    soup = BeautifulSoup(r, 'html.parser')

    nome_veiculo = list()
    for nome in soup.findAll("h2", {"class": "titulo_1"}):
        nome_str = str(nome)
        nome_veiculo.append(nome_str[43:-5])

    origem_veiculo = list()
    for origem in soup.findAll("div", {"class": "visualizacaoDiv-descricao"}):
        origem_str = str(origem)
        posicao1 = (origem_str.find('<b>')) + 3
        posicao2 = (origem_str.find('</b>'))
        origem_veiculo.append(origem_str[posicao1:posicao2])

    km_veiculo = list()
    for km in soup.findAll("div", {"class": "visualizacaoDiv-descricao"}):
        km_str = str(km)
        posicao1 = km_str.find('icon-km icon-large') + 41
        posicao2 = km_str[posicao1:].find('"') + posicao1
        km_veiculo.append(km_str[posicao1:posicao2])

    lance_veiculo = list()
    for lance in soup.findAll("div", {"class": "visualizacaoDiv-lance-desc"}):
        lance_str = str(lance.b)
        posicao1 = lance_str.find('>') + 1
        posicao2 = lance_str.rfind('<')
        lance_veiculo.append(lance_str[posicao1:posicao2])

    combustivel_veiculo = list()
    for combustiveis in soup.findAll("div", {"class": "visualizacaoDiv-descricao"}):
        combustiveis_str = str(combustiveis)
        posicao1 = combustiveis_str.find('<i class="icon-combustivel')
        posicao1 = combustiveis_str[posicao1:].find('<b>') + posicao1 + 3
        posicao2 = combustiveis_str[posicao1:].find('<') + posicao1
        combustivel_veiculo.append(combustiveis_str[posicao1:posicao2])

    cambio_veiculo = list()
    for cambios in soup.findAll("div", {"class": "visualizacaoDiv-descricao"}):
        cambio_str = str(cambios)
        posicao1 = cambio_str.find('class="icon-cambio')
        posicao1 = cambio_str[posicao1:].find('<b>') + posicao1 + 18
        posicao2 = cambio_str[posicao1:].find('<') + posicao1
        cambio_veiculo.append(cambio_str[posicao1:posicao2])

    veiculos_na_pagina = len(nome_veiculo)
    if not retorno:
        for n in range(0, veiculos_na_pagina):
            print(f'{"━" * 70}')
            print(f'{a34}  [{n + 1}] {nome_veiculo[n]}{af}'.center(80))
            print('¨'*70)
            print(f'   Lance▬▬▬▬▬▬▬▬▬▬{lance_veiculo[n]}\n'
                  f'   Origem▬▬▬▬▬▬▬▬▬{origem_veiculo[n]}\n'
                  f'   Combustivel▬▬▬▬{combustivel_veiculo[n]}\n'
                  f'   KM▬▬▬▬▬▬▬▬▬▬▬▬▬{km_veiculo[n]}\n'
                  f'   Cambio▬▬▬▬▬▬▬▬▬{cambio_veiculo[n]}')
    else:
        return veiculos_na_pagina


# corpo
re_do_pograma = 0
print('̶p̶o̶r̶:̶ ̶A̶f̶o̶x̶P̶o̶l̶o̶')
print('▬' * 70)
print(f'{a32}Analisando site por favor aguarde{af}'.center(80))
ldp = leitor_pagina() - 1
ultima_pagina = 1
while True:
    if re_do_pograma == 0:
        print('▬' * 70)
        print(f'O site contem {ldp} Paginas De veículos ativos'.center(70))
        print(f'Digite o numero da pagina desejada ou {a31}"exit"{af} para sair. '.center(80))
        print('▬' * 70)
        pg = input('\033[1;34m>>>: \033[m')
        if pg.isnumeric():
            pg = int(pg)
            if pg in range(1, ldp + 1):
                ultima_pagina = pg
                print(f'{a32}Carregando pagina por favor aguarde...{af}'.center(80))
                pagina()
            else:
                print(f'{a31}ERRO - Pagina inexistente! Digite de 1 a {ldp}.{af}\n')
                continue
        else:
            pg = str(pg).lower().strip()
            if pg == 'exit':
                break
            else:
                print('\033[1;31mERRO - opçao invalida!.\033[m\n')
                continue
    else:
        print('▬' * 70)
        print(f'O site contem {ldp} Paginas De veículos ativos'.center(70))
        print(f'Digite o numero da pagina desejada ou {a31}"exit"{af} para sair'.center(80))
        print(f'Ou {a32}"acessar"{af} para abrir o link do veiculo desejado'.center(80))
        print('▬' * 70)
        pg = input('\033[1;34m>>>: \033[m')
        if pg.isnumeric():
            pg = int(pg)
            if pg in range(1, ldp + 1):
                ultima_pagina = pg
                print(f'{a32}Carregando pagina por favor aguarde...{af}\n\n{"▁" * 191}')
                pagina()
            else:
                print(f'{a31}ERRO - Pagina inexistente! Digite de 1 a {ldp}.{af}\n')
        else:
            pg = str(pg).lower().strip()
            if pg == 'exit':
                break
            elif pg == 'acessar':
                while True:
                    numero_do_veiculo = input(f'{a34}>>>{af} Digite o numero do veiculo ou {a31}"exit"{af} para sair: ')
                    if numero_do_veiculo.isnumeric():
                        numero_do_veiculo = int(numero_do_veiculo)
                        retornos = pagina(True)
                        if numero_do_veiculo in range(1, retornos):
                            link = f'https://www.sodresantoro.com.br/veiculos/ordenacao/data_leilao/tipo-ordenacao/cr' \
                                   f'escente/qtde-itens/15/visualizacao/visual_imagem/item-atual/1/pagina/' \
                                   f'{ultima_pagina}/'
                            req = requests.get(link).text
                            soup_link = BeautifulSoup(req, 'html.parser')
                            link_veiculo = list()
                            for a in soup_link.findAll("div", {"class": "visualizacaoDiv-titulo"}):
                                b = str(a)
                                p1 = b.find('href') + 6
                                p2 = b[p1:].find('"') + p1
                                link_veiculo.append(f'https://www.sodresantoro.com.br{b[p1:p2]}ordenacao/data_leilao/ti'
                                                    f'po-ordenacao/crescente/qtde-itens/15/visualizacao/visual_imagem/i'
                                                    f'tem-atual/1/pagina/1/')
                            link = link_veiculo[numero_do_veiculo - 1]
                            webbrowser.open_new(link)
                            break
                        else:
                            print('ERRO - Digite um numero valido.')
                    else:
                        numero_do_veiculo = numero_do_veiculo.lower().strip()
                        if numero_do_veiculo == 'exit':
                            break
                        else:
                            print('ERRO - opção invalida')
            else:
                print('\033[1;31mERRO - opçao invalida!.\033[m\n')
    re_do_pograma += 1

print(f'{a31}O usuario Finalizou o Progra.{af}')
