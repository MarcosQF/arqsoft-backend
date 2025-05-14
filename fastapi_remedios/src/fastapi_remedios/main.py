from fastapi import FastAPI
from fastapi_remedios.database import Base, engine
from fastapi_remedios.routes import remedios
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CRUD de Remédios")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ou ["*"] para permitir tudo (não recomendado para produção)
    allow_credentials=True,
    allow_methods=["*"],                      # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],                      # Permite todos os headers
)


Base.metadata.create_all(bind=engine)

app.include_router(remedios.router)
