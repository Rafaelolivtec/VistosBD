import Classes_para_importar

print()
print('<<<<<< BEM VINDO AO SISTEMA DE OUVIDORIA CONNECTA >>>>>>')
print()
oc = []
voltarmenu = 1
x = 1
menu = ['1- CADASTRAR OCORRÊNCIAS', '2- LISTAR OCORRÊNCIAS', '3- APAGAR OCORRÊNCIAS', '4- SAIR']
oco = Classes_para_importar.Ouvidoria()
while True:
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[3])
    print()
    opcao = int(input('>>>> DIGITE A OPÇÃO DESEJADA ->'))

    if opcao == 1:
        print()
        ocorrencia = input('>>>> DIGITE SUA OCORRÊNCIA :  ')
        nome = input('>>>> DIGITE SEU NOME : ')
        email = input('>>>> DIGITE SEU EMAIL : ')
        contato = input('>>>> DIGITE SEU NÚMERO P/ CONTATO : ')
        oco.adicionarOcorrencia(ocorrencia,nome,email,contato)

    elif (opcao == 2):

        oco.listarOcorrencias()


    elif (opcao == 3):


        apagar = int(input('SELECIONE A OCORRÊNCIA QUE DESEJA APAGAR // OU DIGITE (0) PARA APAGAR TUDO >>>'))

        oco.apagarRegistro(apagar)

    elif (opcao == 4):
        print()
        print('>>>>>  (( Agradecemos Por Utilizar Nosso Sistema!! ))  <<<<<')
        break
