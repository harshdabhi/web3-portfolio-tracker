from django.shortcuts import render,redirect
from eth_data_files.eth_chain_portfolio import eth_chain_portfolio_data
from credentials.getting_keys import key_data
import  pandas as pd
from eth_transaction_info.eth_latest_transaction import eth_latest_transaction_info

temp=eth_chain_portfolio_data()
temp_api_key=key_data()


# Create your views here.

def homepage(request):
  
    try:
        if request.method=="POST":

            # getting data from html page
            wallet_address=request.POST.get('wallet_address')
            wallet_address=wallet_address.lower()
            api_name=request.POST.get('chain')

            
            data=temp.get_wallet_info(wallet_address,temp_api_key.api_keys(api_name))
            c=temp.final_eth_data(data)
            df=pd.DataFrame(c)
            Total_portfolio_value=df['Amount_usd'].sum()

            d=eth_latest_transaction_info()
            data_transaction=d.get_wallet_transaction_info(wallet_address,temp_api_key.api_keys(api_name))
            final_data_transaction=d.transaction_value(data_transaction)


            context={
                'totalvalue':round(Total_portfolio_value,2),
                'data':c,
                'latest_transaction':final_data_transaction

            }

            return render(request,'homepage.html',context=context)
        
        else:
            return render(request,'homepage.html') 

            
    
    

    except:
        return render(request,'homepage.html') 
        
        


    