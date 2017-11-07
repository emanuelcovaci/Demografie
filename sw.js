var cacheName = "demografie-v4";

var hostname = location.hostname;

var filesToCache = [
  "/",
  "/graphics",
  "/text",
  "/demografia",
  "/tranzitia",
  "/istoric",
  "/donatii",
  "/contact",
  {% for p in static %}"{{p}}",{% endfor %}
  "http://" + hostname + ":3000/countypop",
  "http://" + hostname + ":3000/natalitycounty",
  "http://" + hostname + ":3000/natalitycountyperc",
  "http://" + hostname + ":3000/fertilitycountyperc",
  "http://" + hostname + ":3000/pregnantcounty",
  "http://" + hostname + ":3000/abortions",
  "http://" + hostname + ":3000/abortionsperc",
  "http://" + hostname + ":3000/lifeexpectancy",
  "http://" + hostname + ":3000/lifeexpectancymale",
  "http://" + hostname + ":3000/lifeexpectancyfemale",
  "http://" + hostname + ":3000/misc",
  "http://" + hostname + ":3000/agegrouppop",
  "http://" + hostname + ":3000/population",
  "http://" + hostname + ":3000/agegroupperc",
];

self.addEventListener( "install", function(event) {

  event.waitUntil(
    caches.open( cacheName ).then( function(cache) {
      return cache.addAll( filesToCache.filter(function(k){
        return !k.endsWith("manifest.json");
      }));
    } )
  );
} );

self.addEventListener( "fetch", function(event) {
  event.respondWith(
    caches.open(cacheName).then(function(cache) {
      return cache.match(event.request).then(function(response) {
        if (response) return response;
        var url = event.request.url;
        console.log(url)
        return fetch(event.request).then(function(networkResponse) {
          if(url.startsWith("https://www.google-analytics.com/") ||
             url.endsWith("manifest.json")) return networkResponse;
          cache.put(event.request, networkResponse.clone());
          return networkResponse;
        });
      });
    })
  );
} );

self.addEventListener( "activate", function(e) {
  e.waitUntil(
    caches.keys().then( function(keyList) {
      return Promise.all( keyList.map( function(key) {
        if (key !== cacheName) {
          return caches.delete( key );
        }
      } ) );
    } )
  );
} );