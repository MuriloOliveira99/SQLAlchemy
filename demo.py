class OlaMundo:
    def __enter__(self):
        print('Estou entrando...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Estou saindo...')

with OlaMundo() as ola:
    print('ESTOU AQUI NO MEIO!')

# RESULTADO (METODOS MAGICO)
# Estou entrando...
# ESTOU AQUI NO MEIO!
# Estou saindo...