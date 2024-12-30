from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id":1, "title":"Book 1", "author":"Author 1"},
    {"id":2, "title":"Book 2", "author":"Author 2"},
    {"id":3, "title":"Book 3", "author":"Author 3"},
    {"id":4, "title":"Book 4", "author":"Author 4"},
    {"id":5, "title":"Book 5", "author":"Author 5"},
]

@app.route("/", methods=['GET'])
def home():
    return 'Home page'

#route to get all books
@app.route("/all_books", methods=['GET'])
def get_all_books():
    return jsonify(books)

#route to get specific book by id
@app.route('/books/<int:book_id>', methods=["GET"])
def get_books(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({"error":"book not found"}), 404

#Route to add a new book
@app.route('/books', methods=['POST'])
def add_books():
    new_book = {
        "id" : request.json['id'],
        "title" : request.json['title'],
        "author" : request.json['author'],
    }
    books.append(new_book)
    return jsonify({'message': 'book added successfully'})

#Route to update existing book
@app.route('/update_books/<int:book_id>', methods=["PUT"])
def update_books(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return jsonify({'message':'book updated successfully'})
    return jsonify({"error":"book not found"}), 404

#Route to delete existing book
@app.route('/delete_books/<int:book_id>', methods=["DELETE"])
def delete_books(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message':'book Deleted successfully'})
    return jsonify({"error":"book not found"}), 404


if __name__=='__main__':
    app.run(debug=True)

