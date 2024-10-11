from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository
    service = UsuarioService

    service.criar_usuario("Marta", "marta@gmail.com", "123")


    print("\nListando todos os usuarios.")
    usuarios = service.listar_todos_usuarios()

    for usuario in usuarios:
        print(f"{usuarios.nome} - {usuarios.email}")

    
if __name__ ==  "__main__":
    main()