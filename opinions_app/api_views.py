# what_to_watch/opinions_app/api_views.py

# Импортировать метод jsonify.
from flask import jsonify  

from . import app
from .models import Opinion

# Явно разрешить метод GET.
@app.route('/api/opinions/<int:id>/', methods=['GET'])  
def get_opinion(id):
    # Получить объект по id или выбросить ошибку 404.
    opinion = Opinion.query.get_or_404(id)
    # Конвертировать данные в JSON и вернуть JSON-объект и HTTP-код ответа.
    return jsonify({'opinion': opinion}), 200
