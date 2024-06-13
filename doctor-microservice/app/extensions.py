from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# SQLAlchemy
db = SQLAlchemy()

# CORS
cors = CORS()

# JWT
jwt = JWTManager()
