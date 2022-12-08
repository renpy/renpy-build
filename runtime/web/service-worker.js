var cacheName = 'renpy-web-game';
var filesToCache = [
    '/',
    '/index.html',
    '/game.zip',
    '/renpy-pre.js',
    '/renpy.js',
    '/renpy.data',
    '/renpy.wasm',
    '/web-presplash.jpg'
];

/* Start the service worker and cache all of the app's content or use the existing one */
self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(cacheName).then(function(cache) {
      // Cache files and save etag
      return filesToCache.map(function(url) {
        return fetch(url, { method: 'HEAD' }).then(function(response) {
          caches.match(url).then(function(cached_response) {
            if (cached_response) {
              // If etag is in the response headers, use it to check if the content has changed
              if (response.headers.get('etag')) {
                // Check if content length has changed
                if (response.headers.get('etag') !== cached_response.headers.get('etag')) {
                  console.log('Deleting ' + url + ' from current cache and retrieving it from the server');
                  return cache.delete(url).then(function() {
                    return cache.add(url);
                  });
                } else {
                  // Put existing response into the cache
                  return cache.put(url, cached_response);
                }
              } else if (response.headers.get('content-length')) { // Use content length if etag is not available as a fallback
                // Check if content length has changed
                if (response.headers.get('content-length') !== cached_response.headers.get('content-length')) {
                  console.log('Deleting ' + url + ' from current cache and retrieving it from the server');
                  return cache.delete(url).then(function() {
                    return cache.add(url);
                  });
                } else {
                  // Put existing response into the cache
                  return cache.put(url, cached_response);
                }
              }
            } else {
              // Cache not found, make a call to the server
              return cache.add(url);
            }
          });
        });
      });
    })
  );
  self.skipWaiting();
});

/* Serve cached content when offline */
self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});

/* Delete old caches */
self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keyList) {
      return Promise.all(keyList.map(function(key) {
        if (key !== cacheName) {
          return caches.delete(key);
        }
      }));
    })
  );
  return self.clients.claim();
});