from flask import Flask, request, jsonify
from converter import Converter

app = Flask(__name__)
converter = Converter()

@app.route('/distance', methods=['GET'])
def add():
    try:
        dist = float(request.args.get('value'))
        from_unit = request.args.get('from')
        to_unit = request.args.get('to')
        result = Converter.distance(dist, from_unit, to_unit)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/temperature', methods=['GET'])
def convert_temperature():
    try:
        temp = float(request.args.get('value'))
        from_unit = request.args.get('from')
        to_unit = request.args.get('to')
        
        result = Converter.temperature(temp, from_unit, to_unit)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/weight', methods=['GET'])
def convert_weight():
    try:
        mass = float(request.args.get('value'))
        from_unit = request.args.get('from')
        to_unit = request.args.get('to')
        
        result = Converter.weight(mass, from_unit, to_unit)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)