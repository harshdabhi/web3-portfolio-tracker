from django.shortcuts import render,redirect
from eth_data_files.eth_chain_portfolio import eth_chain_portfolio_data
from credentials.getting_keys import key_data
import  pandas as pd
temp=eth_chain_portfolio_data()
temp_api_key=key_data()


# Create your views here.

def homepage(request):
  
    try:
        if request.method=="POST":
            wallet_address=request.POST.get('wallet_address')
            wallet_address=wallet_address.lower()

            data=temp.get_wallet_info(wallet_address,temp_api_key.api_keys())
            c=temp.final_eth_data(data)
            df=pd.DataFrame(c)
            Total_portfolio_value=df['Amount_usd'].sum()

        

            context={
                'totalvalue':round(Total_portfolio_value,2),
                'data':c,

            }

            return render(request,'homepage.html',context=context)
        
        else:
            return render(request,'homepage.html') 

            
    
    

    except:
        return render(request,'homepage.html') 
        
        


    