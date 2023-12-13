document.getElementById('post-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get post title and content
    var title = document.getElementById('post-title').value;
    var content = document.getElementById('post-content').value;

    // Here you would typically send the data to the server
    // For now, just log it to the console
    console.log('Post Submitted:', title, content);
});