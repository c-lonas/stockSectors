tutBtn = document.getElementById("tutorial");
overlay = document.getElementById("overlay");


tutBtn.addEventListener("click", startTutorial);


function startTutorial() {
    document.addEventListener("keyup", exitTutorial);
    // overlay.setAttribute("style", "display: block");
    jQuery(overlay).fadeIn(300);

    // Instantiate Exit Button
    exitBtn = document.createElement("div");
    exitBtn.classList.add("exit-btn");
    exitBtn.addEventListener("click", clickExitTutorial);
    overlay.appendChild(exitBtn);

    escTxt = document.createElement("p");
    escTxt.classList.add("esc-txt");
    escTxt.innerHTML = "ESC";
    exitBtn.appendChild(escTxt);



    // Instantiate Tip Container
    tipDiv = document.createElement("div");
    tipDiv.classList.add("tip-container");
    overlay.appendChild(tipDiv);

    // Add Tips

    tip1 = document.createElement("p");
    tip1.classList.add("tips");
    tip1.innerHTML = "1) Click a label in the legend to toggle the trace";
    tipDiv.appendChild(tip1);

    tip2 = document.createElement("p");
    tip2.classList.add("tips");
    tip2.innerHTML = "2) Double click a label to solo the trace";
    tipDiv.appendChild(tip2);

    tip3 = document.createElement("p");
    tip3.classList.add("tips");
    tip3.innerHTML = "3) Use the navbar to see stocks from a given sector";
    tipDiv.appendChild(tip3);

    

};


function highlightLegend(){

    // Doesn't work on child objects I guess?
    highlightObj = document.getElementsByClassName("legend")[0];
    console.log(highlightObj);
    jQuery(highlightObj).css({'position': 'relative', 'z-index': "100"});

}

function exitTutorial() {
    let keyName = event.key;
    if (keyName === "Escape") {
        jQuery(overlay).fadeOut(300);
        // overlay.setAttribute("style", "display: none");
        document.removeEventListener("keyup", exitTutorial);
        exitBtn.remove();
        console.log("exited tutorial");
    };
};

function clickExitTutorial() {
    jQuery(overlay).fadeOut(300);
    // overlay.setAttribute("style", "display: none");
    document.removeEventListener("keyup", exitTutorial);
    exitBtn.remove();
    console.log("exited tutorial");
    
};