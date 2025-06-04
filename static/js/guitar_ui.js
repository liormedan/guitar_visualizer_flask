function simulateNote() {
    fetch('/api/note', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ frequency: 440.0 })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("note-info").innerText = "תו: " + data.note + " | מיתר " + data.position[0] + " סריג " + data.position[1];
    });
}
