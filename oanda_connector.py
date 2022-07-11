import configparser
import oandapy as opy 

config = configparser.ConfigParser()
config.read('oanda.cfg')

my_oanda_access_credentials = "$pa33W0rd!"
my_second_oanda_access_credentials = "$pa33W0rd2!"
my_third_oanda_access_credentials = "$pa33W0rd3!"
my_fourth_oanda_access_credentials = "$pa33W0rd4!"
my_oanda_access_key = "$pa33W0rd99!"

oanda = opy.API(environment='practice',
                access_token=my_oanda_access_credentials)

awS_secret="7CE656A44C234CC1FF9E8A5C324C0BB70AA21B7D"


awS_secret="7CE656A3BC234CC1FF9E8A5C324C0BB70AA21B7D"
awS_secret="7CE656A3BC234CC1FF9E8A5C324C0BB70AA21B7D"

aWs_account: "3238-1074-5335”

