from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))

# Desabilitar cache
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Simulação de banco de dados
tickets = [
    {"id": 1, "name": "João", "company": "Empresa A", "system": "RHID", "problem_type": "Erro", "affected_people": 15, "description": "Erro crítico no sistema", "priority": "Alta", "status": "Aberto", "created_at": "2026-03-30 10:00:00", "updated_at": None, "evaluation": None},
    {"id": 2, "name": "Maria", "company": "Empresa B", "system": "WPE", "problem_type": "Lentidão", "affected_people": 5, "description": "Sistema lento", "priority": "Média", "status": "Fechado", "created_at": "2026-03-29 14:00:00", "updated_at": "2026-03-29 16:00:00", "evaluation": 4}
]

def classify_priority(affected_people, problem_type):
    """
    Classifica a prioridade do chamado com base no número de pessoas afetadas e no tipo de problema.
    """
    if affected_people > 10:
        return "Alta"
    if problem_type.lower() == "erro":
        return "Média"
    return "Baixa"

@app.route('/')
def home():
    """
    Rota para a página inicial que renderiza o formulário de criação de chamados.
    """
    return render_template('index.html')

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    """
    Rota para criar um novo chamado.
    """
    try:
        data = request.json
        ticket = {
            'id': len(tickets) + 1,
            'name': data.get('name'),
            'company': data.get('company'),
            'system': data.get('system'),
            'problem_type': data.get('problem_type'),
            'affected_people': data.get('affected_people'),
            'description': data.get('description'),
            'priority': classify_priority(data.get('affected_people'), data.get('problem_type')),
            'status': 'Aberto',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': None,
            'evaluation': None
        }
        tickets.append(ticket)
        return jsonify({'message': 'Chamado criado com sucesso!', 'ticket': ticket}), 201
    except Exception as e:
        return jsonify({'error': 'Erro ao criar chamado', 'details': str(e)}), 400

@app.route('/tickets', methods=['GET'])
def list_tickets():
    """
    Rota para listar todos os chamados criados.
    """
    return jsonify(tickets), 200

@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
    Rota para obter dados do dashboard.
    """
    total_tickets = len(tickets)
    avg_response_time = sum([t['affected_people'] for t in tickets]) / total_tickets if total_tickets > 0 else 0
    avg_evaluation = sum([t['evaluation'] for t in tickets if t['evaluation'] is not None]) / total_tickets if total_tickets > 0 else 0
    delayed_tickets = len([t for t in tickets if t['affected_people'] > 10])

    return jsonify({
        'total_tickets': total_tickets,
        'avg_response_time': avg_response_time,
        'avg_evaluation': avg_evaluation,
        'delayed_tickets': delayed_tickets
    }), 200

if __name__ == '__main__':
    app.run(debug=True)