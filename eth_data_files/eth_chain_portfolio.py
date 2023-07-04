import requests
    

class eth_chain_portfolio_data:

    def __init__(self) -> None:
        pass

    def get_wallet_info(self,wallet_address,api_key):
        '''
        wallet_address: str
        api_key:str 
        return type dictionary 
        
        '''
        wallet_address=wallet_address.lower()
        url = f"https://api.ethplorer.io/getAddressInfo/{wallet_address}?apiKey={api_key}"

        try:
            response = requests.get(url)
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None


    def ETH_info(self,wallet_info):

        '''
        wallet_info:dict,json 
        This function return  data of eth holdings in dict 
        
        '''


        try:

            Eth_dict={
                'Name':'Ethereum',
                'Symbol':'ETH',
                'TokenAddress':None,
                'HolderCount':None,
                'Price':wallet_info['ETH']['price']['rate'],
                'Change24hr':wallet_info['ETH']['price']['diff'],
                'Change7d':wallet_info['ETH']['price']['diff7d'],
                'Token':wallet_info['ETH']['balance'],
                'Amount_usd':(wallet_info['ETH']['balance'])*(wallet_info['ETH']['price']['rate']) }
            return Eth_dict
        except:

            pass


    def altcoin_info(self,wallet_info):

        '''
        wallet_info:dict
        return type dictionary
        
        
        '''
        transactions=wallet_info

        try:
            
            dict_info={
                'Name': transactions['tokenInfo']['name'],
                'Symbol': transactions['tokenInfo']['symbol'],
                'TokenAddress':transactions['tokenInfo']['address'],
                'HolderCount':transactions['tokenInfo']['holdersCount'],
                'Price':transactions['tokenInfo']['price']['rate'],
                'Change24hr':transactions['tokenInfo']['price']['diff'],
                'Change7d':transactions['tokenInfo']['price']['diff7d'],
                'Token':int(transactions['rawBalance'])/10**18,
                'Amount_usd':round((int(transactions['rawBalance'])/10**18)*(transactions['tokenInfo']['price']['rate']),2)
            }

            return dict_info
        except:
            pass
        

    def final_eth_data(self,wallet_info):    
        temp_values=[self.altcoin_info(i) for i in wallet_info['tokens']]
        final_values=[i for i in temp_values if i is not None]
        final_values.append(self.ETH_info(wallet_info))

        return final_values






#wallet_info = get_wallet_info(wallet_address,api_keys)

