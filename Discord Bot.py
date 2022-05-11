from get_all_tickers import get_tickers 

DATE1= 'type date 1'
DATE2= 'type date 2'
tickers= ['qqq','spy','aal','lcid','bynd']

#gerenciar mensagens do canal
def gerenciador_mensagem(input_test):
    
    message= (input_test).lower().split()
    stock_to_buy = filtro_stocks(input_test)

    if 'calls' in message or 'puts' in message:
        if stock_to_buy == 'spy' or stock_to_buy == 'qqq':  
            return 'BTO' + stock_to_buy + DATE2
        else:  
            return 'BTO' + stock_to_buy + DATE1
    
    else:  
        return None


#Verificar se a palavra está na função
def filtro_stocks(message):

    split_message= (message).lower().split()
    lastticker= None

    for word in split_message:
        if word in tickers:
            lastticker= word
    return lastticker   

print(filtro_stocks('uma casa QQQ vou spy aviao'))