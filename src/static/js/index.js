import { addKeywordCookie, getKeywordCookie, removeKeywordCookie } from "./utils.js";

document.getElementById("keyword-form").addEventListener("submit", (event)=>{
    addKeywordCookie(event);
    makeKeywordsList();
});
makeKeywordsList();

let cookieString = "keywords=";
function loading() {
    document.getElementById("content").style.display = "none";
    document.getElementById("loading").style.display = "block";
}

function makeKeywordsList() {
    let keywords = getKeywordCookie().split(",");
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
            removeButton.onclick = function(){
                removeKeywordCookie(keyword);
                makeKeywordsList();
            };
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