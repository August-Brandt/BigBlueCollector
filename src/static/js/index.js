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

function removeKeywordCookie(removekeyword) {
    console.log("removing " + removekeyword);
    let keywords = getCookie("keywords").split(",");
    finalCookie = "keywords=";
    keywords.forEach((keyword) =>  {
        if (keyword != removekeyword) {
            finalCookie += keyword + ",";
        }
    });
    document.cookie = finalCookie[finalCookie.length-1] == "," ? finalCookie.slice(0, -1) + ";" : finalCookie;
    makeKeywordsList();
}

function makeKeywordsList() {
    let keywords = getCookie("keywords").split(",");
    let list = document.getElementById("keywords-list");
    list.innerHTML = "";
    keywords.forEach((keyword) => {
        if (keyword != "") {
            // Create the html for a keyword with remove button
            let elemn = document.createElement('li');
            let elemnWrapper = document.createElement('div');
            elemnWrapper.className = "elemnWrapper";
            let removeButton = document.createElement('button');
            removeButton.innerHTML = "X";
            removeButton.className = "removeKWbutton";
            removeButton.onclick = function(){removeKeywordCookie(keyword)};
            elemnWrapper.appendChild(removeButton);
            let keywordElemn = document.createElement('p');
            keywordElemn.innerHTML = keyword;
            keywordElemn.className = "keywordName";
            elemnWrapper.appendChild(keywordElemn);
            elemn.appendChild(elemnWrapper);
            
            // Add new keyword to list on page
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