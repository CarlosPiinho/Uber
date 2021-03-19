pessoas = int(input('Quantas pessoas irão com a gente? ')).sprit
cidade = str(input('Qual praia você(s) deseja(m) conhecer hoje? ')).
print('Calculando...')


joaquina = (32.5 * .5) * pessoas
campeche = (35 * .5) * pessoas
ingleses = (15 * .5) * pessoas
daniela = (15.4 * .5) * pessoas
lagoinha = (47.7 * .5) * pessoas

if cidade == 'joaquina':
     print('===============================================================')
     print('A sua corrida para a praia da Joaquina vai custar R${:.2f}'.format(joaquina))
     print('O valor fica R${:.2f} por pessoa.'.format(joaquina/pessoas))
     print('===============================================================')

elif cidade == 'campeche':
     print('===============================================================')
     print('A sua corrida para a praia do Campeche vai custar R${:.2f}'.format(campeche))
     print('O valor fica R${:.2f} por pessoa.'.format(campeche/pessoas))
     print('===============================================================')
    
elif cidade == 'ingleses':
     print('===============================================================')
     print('A sua corrida para a praia do Ingleses vai custar R${:.2f}'.format(ingleses))
     print('O valor fica R${:.2f} por pessoa.'.format(ingleses/pessoas))
     print('===============================================================')
    
elif cidade == 'daniela':
     print('===============================================================')
     print('A sua corrida para a praia do Daniela vai custar R${:.2f}'.format(daniela))
     print('O valor fica R${:.2f} por pessoa.'.format(daniela/pessoas))
     print('===============================================================')

elif cidade == 'lagoinha':
    print('=========================================================')
    print('A sua corrida para a praia do Lagoinha do leste vai custar R${:.2f}'.format(lagoinha))
    print('O valor fica R${:.2f} por pessoa.'.format(lagoinha/pessoas))
    print('=========================================================')

else:
    print('=========================================================')
    print('                    ATENÇÃO!!!                    ')
    print('Ainda não realizamos corridas para está praia')
    print('=========================================================')



