//
//navbar
//
// Wait for the entire document to be ready
document.addEventListener("DOMContentLoaded", function() {
    // Get the placeholder div
    var placeholderDiv = document.getElementById("navbar-insert");

    // Fetch content from another document
    fetch('/content/navbar.html')
        .then(response => response.text())
        .then(data => {
            // Create a temporary div to hold the fetched content
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = data;

            // Get the content you want to insert
            var dynamicContent = tempDiv.querySelector('#navbar');

            // Append the dynamic content to the placeholder div
            placeholderDiv.appendChild(dynamicContent);
        })
        .catch(error => console.error('Error fetching content:', error));
});
//
//footer
//
//for min height and center item
function footerheight(){
    let foot_height=document.getElementById("footer").clientHeight +"px";
    var r = document.querySelector(':root');
    r.style.setProperty("--footer-height", foot_height);
}
function footertxtright(){
    var footerTextContainer = document.querySelector('.foot_txt_right');

        if (footerVariant === 'std') {
            footerTextContainer.innerHTML = 'WIP - website not finished';
        } else if (footerVariant === 'blog') {
            footerTextContainer.innerHTML = 'add license etc here';
        } else if (footerVariant === 'error') {
            footerTextContainer.innerHTML = '<a href="https://github.com/jakjakob/jakjakobdoteu/issues/new">Report an Issue</a>';
        }
}
// Wait for the entire document to be ready
document.addEventListener("DOMContentLoaded", function() {
    // Get the placeholder div
    var placeholderDiv = document.getElementById("footer-insert");

    // Fetch content from another document
    fetch('/content/footer.html')
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
            footertxtright();
        })
        .catch(error => console.error('Error fetching content:', error));
});
window.addEventListener('resize', function() {footerheight();});