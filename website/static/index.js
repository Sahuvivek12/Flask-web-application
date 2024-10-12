function deleteNote(noteId) {
    console.log("Attempting to delete note with ID:", noteId);  // Debug log
    fetch('/delete-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Set the correct content type
        },
        body: JSON.stringify({ noteId: noteId }),  // Send the noteId as JSON
    }).then((res) => {
        if (res.ok) {
            window.location.href = "/";  // Redirect if successful
        } else {
            console.error("Failed to delete note:", res);  // Log error if not ok
        }
    }).catch((error) => {
        console.error("Error occurred during fetch:", error);  // Catch any network errors
    });
}
