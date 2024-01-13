//for min height and center item
function footerheight(){
    let foot_height=document.getElementById("footer").clientHeight +"px";
    var r = document.querySelector(':root');
    r.style.setProperty("--footer-height", foot_height);
}
window.addEventListener('resize', function() {footerheight();});