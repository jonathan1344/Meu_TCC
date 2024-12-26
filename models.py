from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.usuario}>'

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(20), nullable=False, unique=True)
    razao_social = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=True)
    cidade = db.Column(db.String(50), nullable=True)
    uf = db.Column(db.String(2), nullable=True)
    cep = db.Column(db.String(10), nullable=True)
    pais = db.Column(db.String(50), nullable=True)
    necessario_po = db.Column(db.Boolean, nullable=True)
    projeto_principal = db.Column(db.String(100), nullable=True)
    tipo_contrato = db.Column(db.Enum('comum', 'especial'), nullable=True)
    moeda = db.Column(db.String(10), nullable=True)
    movimentacao = db.Column(db.String(50), nullable=True)
    seguro = db.Column(db.Boolean, nullable=True)
    fat_min_hora = db.Column(db.Numeric(10, 2), nullable=True)
    analise_nc = db.Column(db.String(50), nullable=True)
    rebate = db.Column(db.Numeric(5, 2), nullable=True)
    abertura_projeto = db.Column(db.String(50), nullable=True)
    reatividade = db.Column(db.String(50), nullable=True)
    percentual_he_semana = db.Column(db.Numeric(5, 2), nullable=True)
    administrativo = db.Column(db.String(50), nullable=True)
    frete = db.Column(db.Numeric(10, 2), nullable=True)
    percentual_he_sabado = db.Column(db.Numeric(5, 2), nullable=True)
    warehouse = db.Column(db.String(50), nullable=True)
    percentual_he_domingo = db.Column(db.Numeric(5, 2), nullable=True)
    percentual_ad_noturno = db.Column(db.Numeric(5, 2), nullable=True)

    def __repr__(self):
        return f'<Cliente {self.razao_social}>'
