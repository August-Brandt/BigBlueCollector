document.getElementById("keyword-form").addEventListener("submit", addKeywordCookie);
makeKeywordsList();

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

function makeKeywordsList() {
    let keywords = getCookie("keywords").split(",");
    let list = document.getElementById("keywords-list");
    list.innerHTML = "";
    keywords.forEach((keyword) => {
        if (keyword != "") {
            let elemn = document.createElement('li');
            elemn.innerHTML = keyword;
            list.appendChild(elemn); 
        }
    });
}

function addKeywordCookie(event) {
    console.log(event.target.keyword);
    // event.preventDefault();
    event.preventDefault();
    let cvalue = event.target.keyword.value;
    console.log(cvalue);
    let prevString = getCookie("keywords");
    console.log("prevstring: " + prevString);
    let cookieString = ""; 
    if (prevString == "") {
        console.log("Adding " + cvalue + " to cookies");
        cookieString = "keywords=" + cvalue + ";"
    } else {
        console.log("Other log");
        cookieString = "keywords=" + prevString + "," + cvalue + ";";
    }
    console.log(cookieString);
    document.cookie = cookieString;
    makeKeywordsList();
    document.getElementById("title-keyword").value = "";
}