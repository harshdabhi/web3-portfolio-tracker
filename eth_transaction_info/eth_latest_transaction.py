import datetime
import requests

class eth_latest_transaction_info:
    def __init__(self) -> None:
         pass
    
    def get_wallet_transaction_info(self,wallet_address,api_key):
            '''
            wallet_address: str
            api_key:str 
            return type dictionary 
            
            '''
            wallet_address=wallet_address.lower()
            url = f"https://api.ethplorer.io/getAddressHistory/{wallet_address}?apiKey={api_key}&limit=1000"

            try:
                response = requests.get(url)
                data = response.json()
                return data
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")
                return None
            
            
    def transaction_value(self,data):
        data=c['operations']
        final_value={
            'timestamp':datetime.datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
            'token_address':data['tokenInfo']['address'],
            'symbol':data['tokenInfo']['symbol'],
            'price':data['tokenInfo']['price']['rate'],
            'value':int(data['value'])/10**18,
            'from':data['from'],
            'to':data['to'],

            }
        return data
    
    def __str__(self) -> str:
        return "This class return last 1000 transaction info of wallet address"