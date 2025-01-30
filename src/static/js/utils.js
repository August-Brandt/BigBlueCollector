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

export function getKeywordCookie() {
    return getCookie("keywords");
}

export function removeKeywordCookie(removekeyword) {
    console.log("removing " + removekeyword);
    let keywords = getKeywordCookie().split(",");
    let finalCookie = "keywords=";
    keywords.forEach((keyword) =>  {
        if (keyword != removekeyword) {
            finalCookie += keyword + ",";
        }
    });
    document.cookie = finalCookie[finalCookie.length-1] == "," ? finalCookie.slice(0, -1) + ";" : finalCookie;
}

export function addKeywordCookie(event) {
    console.log(event.target.keyword);
    // event.preventDefault();
    event.preventDefault();
    let cvalue = event.target.keyword.value;
    console.log(cvalue);
    let prevString = getCookie("keywords");
    
    // Make sure identical keywords are not added
    if (prevString.split(",").includes(cvalue)) {
        alert("Keyword is already in list\n\nPlease enter a new different keyword");
        return;
    }

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
    document.getElementById("title-keyword").value = "";
}