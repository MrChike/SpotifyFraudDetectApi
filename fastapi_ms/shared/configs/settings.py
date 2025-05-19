from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class AppSettings(BaseSettings):
    app_name: str 
    secret_key: str 
    database_url: str
    contact_name: str
    contact_info: str


app_settings = AppSettings() # type: ignore
