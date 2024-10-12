function deleteNote(noteId) {
    fetch(`/delete-note/${noteId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrf_token')
        }
    })
    .then((response) => {
        if (response.ok) {
            window.location.reload();
        } else {
            console.error('Error deleting note:', response.statusText);
        }
    })
    .catch((error) => {
        console.error('Fetch error:', error);
    });
}
