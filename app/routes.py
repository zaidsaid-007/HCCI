from app import app, db
from flask import request, jsonify
from app.models import User, Company, Agency, Worker

# Register a new user
@app.route('/register/user', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Register a new company
@app.route('/register/company', methods=['POST'])
def register_company():
    data = request.get_json()
    new_company = Company(name=data['name'], address=data['address'])
    db.session.add(new_company)
    db.session.commit()
    return jsonify({'message': 'Company registered successfully'}), 201

# Register a new agency
@app.route('/register/agency', methods=['POST'])
def register_agency():
    data = request.get_json()
    new_agency = Agency(name=data['name'], address=data['address'])
    db.session.add(new_agency)
    db.session.commit()
    return jsonify({'message': 'Agency registered successfully'}), 201

# Register a new worker
@app.route('/register/worker', methods=['POST'])
def register_worker():
    data = request.get_json()
    new_worker = Worker(name=data['name'], gender=data['gender'], dob=data['dob'],
                        agency_id=data['agency_id'], company_id=data['company_id'])
    db.session.add(new_worker)
    db.session.commit()
    return jsonify({'message': 'Worker registered successfully'}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

# Get all companies
@app.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return jsonify([company.serialize() for company in companies]), 200

# Get all agencies
@app.route('/agencies', methods=['GET'])
def get_agencies():
    agencies = Agency.query.all()
    return jsonify([agency.serialize() for agency in agencies]), 200

# Get all workers
@app.route('/workers', methods=['GET'])
def get_workers():
    workers = Worker.query.all()
    return jsonify([worker.serialize() for worker in workers]), 200

# Delete a user by ID
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200
