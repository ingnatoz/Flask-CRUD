from flask import Blueprint, jsonify, request

from models.Book import Book, BookSchema
from utils.db import db

# Routes
book_r = Blueprint("Book-Route", __name__)


@book_r.route('/', methods=['GET'])
def home():
    data = {'message': 'home'}
    return jsonify(data)


# Create Tables
@book_r.route('/generate_migration', methods=['GET'])
def migrations():
    db.drop_all()
    db.create_all()
    data = {'message': 'migrations ok!'}
    return jsonify(data)


# Get All Books
@book_r.route('/book', methods=['GET'])
def get_books():
    books = Book.get_all()
    serializer = BookSchema(many=True)
    data = serializer.dump(books)
    # db.session.close()
    return jsonify(data), 200


# Create Book
@book_r.route('/book', methods=['POST'])
def create_a_book():
    data = request.get_json()

    new_book = Book(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price'),
        quantity=data.get('quantity')
    )
    new_book.save()
    serializer = BookSchema()
    data = serializer.dump(new_book)
    return jsonify(data), 201


# Get by id
@book_r.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.get_by_id(id)
    serializer = BookSchema()
    data = serializer.dump(book)
    return jsonify(data), 200


# update by id
@book_r.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book_to_update = Book.get_by_id(id)
    book_to_update.name = data.get('name')
    book_to_update.description = data.get('description')
    book_to_update.price = data.get('price')
    book_to_update.quantity = data.get('quantity')
    db.session.commit()
    serializer = BookSchema()
    book_data = serializer.dump(book_to_update)
    return jsonify(book_data), 200


# delete by id
@book_r.route('/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    book_to_delete = Book.get_by_id(id)
    book_to_delete.delete()
    return jsonify({"message": "Deleted"}), 200


@book_r.app_errorhandler(404)
def handle_404(err):
    result = {'error': '404'}
    return jsonify(result)


@book_r.app_errorhandler(500)
def handle_500(err):
    result = {'error': '500'}
    return jsonify(result)
