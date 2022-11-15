class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'tt-serverapi.mysql.database.azure.com'
    MYSQL_USER = 'usuario'
    MYSQL_PASSWORD = 'Tt202212345678'
    MYSQL_DB = 'places'
    MYSQL_PORT = 3306


config = {
    'development': DevelopmentConfig
}