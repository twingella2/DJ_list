from dotenv import load_dotenv                                                                                                                                                      
import os                                                                                                                                                                           
                                                                                                                                                                                    
load_dotenv('.env_sample')  # you have to specify the path to your .env file if it's not in the same directory                                                                      
                                                                                                                                                                                    
CLIENT_ID = os.getenv('CLIENT_ID')                                                                                                                                                  
CLIENT_SECRET = os.getenv('CLIENT_SECRET')                                                                                                                                          
REDIRECT_URI = os.getenv('REDIRECT_URI')                                                                                                                                            
                                                                                                                                                                                    
print(f"CLIENT_ID: {CLIENT_ID}")                                                                                                                                                    
print(f"CLIENT_SECRET: {CLIENT_SECRET}")                                                                                                                                            
print(f"REDIRECT_URI: {REDIRECT_URI}") 