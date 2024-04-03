from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GOOGLE_APPLICATION_CREDENTIALS:str = 'XXX'
    secret_key: str = 'XXX!'  # Replace with your actual secret key
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///users.db'  # Example for SQLite
    SQLALCHEMY_BINDS = {
        'predictions': 'sqlite:///predictions.db',  # Secondary database
        'rate_limits': 'sqlite:///ratelimits.db'  # New database for rate limits
        }
    SECURITY_PASSWORD_SALT: str = 'XXX'

    stripeAPI_publishableKey: str = "XXX"
    stripeAPI_secretkey: str = "XXX"

    test_stripeAPI_publishableKey: str = "XXX"
    test_stripeAPI_secretkey: str = "XX"

    STRIPE_PUBLIC_KEY: str = stripeAPI_publishableKey
    STRIPE_SECRET_KEY: str = stripeAPI_secretkey
    TEST_STRIPE_PUBLIC_KEY: str = test_stripeAPI_publishableKey
    TEST_STRIPE_SECRET_KEY: str = test_stripeAPI_secretkey

    stripe_api_key: str = 'XXXXXX_API_KEY'


settings = Settings()  # type: ignore

# import os

# class Config:
#     DB_CONFIG = os.getenv(
#         "DB_CONFIG",
#         "postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}".format(
#             DB_USER=os.getenv("DB_USER", "fastapi"),
#             DB_PASSWORD=os.getenv("DB_PASSWORD", "fastapi-password"),
#             DB_HOST=os.getenv("DB_HOST", "fastapi-postgresql:5432"),
#             DB_NAME=os.getenv("DB_NAME", "fastapi"),
#         ),
#     )


# config = Config