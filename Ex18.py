#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho=float(input('Tamanho do arquivo:MB'))
velocidade=float(input('Velocidade da internet:Mbps'))
tempo=(tamanho/(velocidade/8))/60
print(f'O download levará {tempo:.2f} minuto(s)')