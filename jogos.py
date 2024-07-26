import pandas as pd
encoding='latin1'
encoding='ISO-8859-1'
encoding='utf-8'

produto = pd.read_excel(r'Pasta3.xlsx')
print(produto)
logic= "1"


for produt in produto['x5']:
    for i in range(1):
        perg = input(" Qual o valor de {} = ".format(produt))
        perg= int(perg)
        #for produ in produto['Rx5']:
            #if produto['Rx5'] == perg:
                #print("muito bem")
                #break
            #else:
                #print("voce errou, boa sorte na proxima vez")


