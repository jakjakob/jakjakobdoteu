// Wait for the entire document to be ready
document.addEventListener("DOMContentLoaded", function() {
    // Get the placeholder div
    var placeholderDiv = document.getElementById("footer-insert");

    // Fetch content from another document
    fetch('/content/footer-std.html')
        .then(response => response.text())
        .then(data => {
            // Create a temporary div to hold the fetched content
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = data;

            // Get the content you want to insert
            var dynamicContent = tempDiv.querySelector('#footer');

            // Append the dynamic content to the placeholder div
            placeholderDiv.appendChild(dynamicContent);

            footerheight();
        })
        .catch(error => console.error('Error fetching content:', error));
});