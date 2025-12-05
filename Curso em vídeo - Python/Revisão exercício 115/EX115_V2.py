# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from modulos_sistemas import cadastro_design,dados_manipul

while True:
    n = cadastro_design.header_conf('Menu Principal')
    try:
        nome = str(input('Digite o nome do arquivo a ser lido: '))
    except KeyboardInterrupt:
        print('\033[0:31mVocê desejou sair do programa\033[m')
        raise
    except:
        print('\033[0:33mHouve um problema ao continuar. Tente novamente.\033[m')
        continue
    else:
        print(f'A opção digitada é{n}')
        if n == 1:
            status = dados_manipul.arq_existe(nome)
            if status is False:
                print('Deseja criar arquivo?')
        elif n == 2:
            print('\033[0:31mArquivo existe\033[m')
        elif n == 3:
            print('\033[0:33mSaindo do programa...\033[m')
            break
        else:
            print('Opção invalida. Tente novamente.')

