from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/note', methods=['POST'])
def detect_note():
    data = request.json
    freq = data.get('frequency')
    note = get_note_from_freq(freq)
    string_fret = map_note_to_guitar(note)
    return jsonify({'note': note, 'position': string_fret})

def get_note_from_freq(freq):
    import math
    A4 = 440.0
    if freq <= 0:
        return ""
    n = round(12 * math.log2(freq / A4))
    note_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    octave = 4 + (n + 9) // 12
    name = note_names[(n + 9) % 12]
    return f"{name}{octave}"

def map_note_to_guitar(note):
    guitar_map = {
        'E4': (1, 0), 'F4': (1, 1), 'G4': (1, 3),
        'A4': (2, 2), 'B4': (2, 4), 'C5': (2, 5),
        'D4': (3, 0), 'E5': (3, 2), 'F5': (3, 3),
        'G3': (4, 0), 'A3': (4, 2), 'B3': (4, 4),
        'E2': (6, 0), 'G2': (6, 3), 'A2': (6, 5)
    }
    return guitar_map.get(note, (0, 0))

if __name__ == '__main__':
    app.run(debug=True)
