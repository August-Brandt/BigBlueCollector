document.getElementById("keyword-form").addEventListener("submit", addKeywordCookie);

let cookieString = "keywords=";
function loading() {
    document.getElementById("content").style.display = "none";
    document.getElementById("loading").style.display = "block";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }
    return "";
}

function addKeywordCookie(event) {
    console.log(event.target.keyword);
    // event.preventDefault();
    let cvalue = event.target.keyword.value;
    console.log(cvalue);
    let prevstring = getCookie("keywords");
    console.log("prevstring: " + prevstring);
    let cookieString = ""; 
    if (prevstring == "") {
        console.log("Adding " + cvalue + " to cookies");
        cookieString = "keywords=" + cvalue + ";"
    } else {
        console.log("Other log");
        cookieString = "keywords=" + prevstring + "," + cvalue + ";";
    }
    console.log(cookieString);
    document.cookie = cookieString;
}