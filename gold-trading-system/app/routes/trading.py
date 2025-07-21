from flask import Blueprint, request, jsonify
from app.routes.auth import token_required
from app.models.transaction import Transaction
from run import db

trading_bp = Blueprint('trading', __name__)

@trading_bp.route('/buy', methods=['POST'])
@token_required
def buy_gold(current_user):
    data = request.get_json()
    gold_id = data.get('gold_id')
    amount = data.get('amount')
    price = data.get('price')

    if not gold_id or not amount or not price:
        return jsonify({'message': 'Missing gold_id, amount, or price'}), 400

    transaction = Transaction(
        user_id=current_user.id,
        gold_id=gold_id,
        transaction_type='buy',
        amount=amount,
        price=price
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Buy order placed successfully'}), 201

@trading_bp.route('/sell', methods=['POST'])
@token_required
def sell_gold(current_user):
    data = request.get_json()
    gold_id = data.get('gold_id')
    amount = data.get('amount')
    price = data.get('price')

    if not gold_id or not amount or not price:
        return jsonify({'message': 'Missing gold_id, amount, or price'}), 400

    transaction = Transaction(
        user_id=current_user.id,
        gold_id=gold_id,
        transaction_type='sell',
        amount=amount,
        price=price
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Sell order placed successfully'}), 201
