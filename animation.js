// Page fade animation
window.onload = function(){

document.body.style.opacity = "0";

setTimeout(function(){
document.body.style.transition = "opacity 1.5s";
document.body.style.opacity = "1";
},100);

};


// Floating doctor icon speed change
function startAnimation(){

let icon=document.querySelector(".med-icon");

if(icon){
icon.style.animationDuration="12s";
}

}


// Heartbeat effect
function heartbeatEffect(){

let beat=document.querySelector(".heartbeat");

if(beat){

setInterval(function(){

beat.style.background="red";

setTimeout(function(){
beat.style.background="darkred";
},300);

},1000);

}

}


// Start animations
startAnimation();
heartbeatEffect();