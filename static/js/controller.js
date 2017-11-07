var serviceWorkerPath = "/sw.js";
var serviceWorker = registerServiceWorker( serviceWorkerPath );

function registerServiceWorker(serviceWorkerPath) {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker
             .register( serviceWorkerPath )
             .then(
               function(reg) {
                 console.log( "charcha service worker registered" );
               }
             ).catch( function(error) {
      console.log( error );
    } );
  }
}