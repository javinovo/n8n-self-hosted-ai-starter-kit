from flask import Flask, request, send_file, jsonify
import subprocess
import os

app = Flask(__name__)
SHARED_DIR = '/data/shared'

@app.route('/convert', methods=['POST'])
def convert_doc():
    # Option 1: Accept filename (safer for container internal use)
    filename = request.json.get('filename')
    if not filename or not filename.endswith('.doc'):
        return jsonify({'error': 'Valid .doc filename must be provided'}), 400
    input_path = os.path.join(SHARED_DIR, filename)
    output_filename = filename.rsplit('.', 1)[0] + '.txt'
    output_path = os.path.join(SHARED_DIR, output_filename)

    try:
        with open(output_path, 'w') as out_file:
            subprocess.run(['antiword', input_path], stdout=out_file, check=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
