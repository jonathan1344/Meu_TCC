from flask import Flask, render_template, request, redirect, session, jsonify, flash
from config import Config
from models import db, User, Cliente  # Certifique-se de que o modelo Cliente está definido
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'supersecretkey'  # Adicione uma chave secreta

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    erro = ""
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if not usuario:
            erro = "Preencha seu nome de usuário!<br>"
        elif not senha:
            erro = "Preencha sua senha!<br>"
        else:
            user = User.query.filter_by(usuario=usuario).first()
            if user and user.senha == senha:
                session['id'] = user.id
                session['nome'] = user.usuario
                return redirect('/painel')
            else:
                erro = "Falha ao logar! Senha ou usuário incorreto!<br>"

    return render_template('index.html', erro=erro)

@app.route('/painel')
def painel():
    if not session.get('id'):
        return redirect('/')  # Redireciona para a página de login se não estiver autenticado
    nome = session.get('nome', 'Usuário')
    return render_template('painel.html', nome=nome)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    if not session.get('id'):
        return redirect('/')  # Redireciona para a página de login se não estiver autenticado

    mensagem_sucesso = ''
    if request.method == 'POST':
        # Captura os dados do formulário
        cnpj = request.form.get('cnpj')
        razao_social = request.form.get('razao_social')
        endereco = request.form.get('endereco')
        cidade = request.form.get('cidade')
        uf = request.form.get('uf')
        cep = request.form.get('cep')
        pais = request.form.get('pais')
        necessario_po = request.form.get('necessario_po') == 'on'  # Checkbox
        projeto_principal = request.form.get('projeto_principal')
        tipo_contrato = request.form.get('tipo_contrato')
        moeda = request.form.get('moeda')
        movimentacao = request.form.get('movimentacao')
        seguro = request.form.get('seguro') == 'on'  # Checkbox
        fat_min_hora = request.form.get('fat_min_hora')
        analise_nc = request.form.get('analise_nc')
        rebate = request.form.get('rebate')
        abertura_projeto = request.form.get('abertura_projeto')
        reatividade = request.form.get('reatividade')
        percentual_he_semana = request.form.get('percentual_he_semana')
        administrativo = request.form.get('administrativo')
        frete = request.form.get('frete')
        percentual_he_sabado = request.form.get('percentual_he_sabado')
        warehouse = request.form.get('warehouse')
        percentual_he_domingo = request.form.get('percentual_he_domingo')
        percentual_ad_noturno = request.form.get('percentual_ad_noturno')

        # Criação do novo cliente
        novo_cliente = Cliente(
            cnpj=cnpj,
            razao_social=razao_social,
            endereco=endereco,
            cidade=cidade,
            uf=uf,
            cep=cep,
            pais=pais,
            necessario_po=necessario_po,
            projeto_principal=projeto_principal,
            tipo_contrato=tipo_contrato,
            moeda=moeda,
            movimentacao=movimentacao,
            seguro=seguro,
            fat_min_hora=fat_min_hora,
            analise_nc=analise_nc,
            rebate=rebate,
            abertura_projeto=abertura_projeto,
            reatividade=reatividade,
            percentual_he_semana=percentual_he_semana,
            administrativo=administrativo,
            frete=frete,
            percentual_he_sabado=percentual_he_sabado,
            warehouse=warehouse,
            percentual_he_domingo=percentual_he_domingo,
            percentual_ad_noturno=percentual_ad_noturno
        )

        try:
            db.session.add(novo_cliente)
            db.session.commit()
            mensagem_sucesso = "Cliente cadastrado com sucesso!"
        except IntegrityError:
            db.session.rollback()
            mensagem_sucesso = "Erro ao cadastrar cliente: CNPJ já cadastrado ou dados inválidos."

    return render_template('cadastro_cliente.html', mensagem_sucesso=mensagem_sucesso)

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    if not session.get('id'):
        return redirect('/')  # Redireciona para a página de login se não estiver autenticado
    nome = request.json.get('nome')
    clientes = Cliente.query.filter(Cliente.razao_social.ilike(f"%{nome}%")).all()
    resultados = [
        {
            'id': cliente.id,
            'cnpj': cliente.cnpj,
            'razao_social': cliente.razao_social,
            'endereco': cliente.endereco,
            'cidade': cliente.cidade,
            'uf': cliente.uf,
            'cep': cliente.cep,
            'pais': cliente.pais,
            'necessario_po': cliente.necessario_po,
            'projeto_principal': cliente.projeto_principal,
            'tipo_contrato': cliente.tipo_contrato,
            'moeda': cliente.moeda,
            'movimentacao': cliente.movimentacao,
            'seguro': cliente.seguro,
            'fat_min_hora': cliente.fat_min_hora,
            'analise_nc': cliente.analise_nc,
            'rebate': cliente.rebate,
            'abertura_projeto': cliente.abertura_projeto,
            'reatividade': cliente.reatividade,
            'percentual_he_semana': cliente.percentual_he_semana,
            'administrativo': cliente.administrativo,
            'frete': cliente.frete,
            'percentual_he_sabado': cliente.percentual_he_sabado,
            'warehouse': cliente.warehouse,
            'percentual_he_domingo': cliente.percentual_he_domingo,
            'percentual_ad_noturno': cliente.percentual_ad_noturno
        } for cliente in clientes
    ]
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
