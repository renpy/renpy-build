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

install = async () => {
    var cache = await caches.open(cacheName);
    var catalog_response = await fetch('/pwa_catalog.json');
    // copy the response so we can save it to cache
    var catalog_response_copy = catalog_response.clone();
    // Check if response is valid
    if (catalog_response.status === 200) {
        var pwa_catalog = await catalog_response.json();
        var cached_pwa_response = await caches.match('/pwa_catalog.json');
        // Get the response as json or set it as empty
        var cached_pwa_catalog = null;
        if (cached_pwa_response === undefined) {
            cached_pwa_catalog = { "core": {} };
        } else {
            // Set response to cached_pwa_catalog
            var cached_pwa_catalog = await cached_pwa_response.json();
        }

        for (var i = 0; i < filesToCache.length; i++) {
            var url = filesToCache[i];
            var cached_response = await caches.match(url);
            var stripped_url = url.replace("/", "")
            if (stripped_url == "") {
                // If url is root, set it to index.html
                stripped_url = "index.html"
            }
            if (cached_response) {
                // Make sure the file is present in pwa_catalog.json
                if (pwa_catalog["core"][stripped_url] !== undefined) {
                    // Check if md5 hash has changed
                    if (cached_pwa_catalog["core"][stripped_url] !== pwa_catalog["core"][stripped_url]) {
                        console.log('Deleting ' + url + ' from current cache and retrieving it from the server');
                        await cache.delete(url)
                        await cache.add(url);
                    } else {
                        // Put existing response into the cache
                        await cache.put(url, cached_response);
                    }
                }
            } else {
                // Cache not found, make a call to the server
                await cache.add(url);
            }
        }
        // Save pwa_catalog.json to cache
        await cache.put('/pwa_catalog.json', catalog_response_copy);
    }
}

/* Start the service worker and cache all of the app's content or use the existing one */
self.addEventListener('install', function (e) {
    e.waitUntil(
        install()
    );
    self.skipWaiting();
});


/* Serve cached content when offline */
self.addEventListener('fetch', function (e) {
    e.respondWith(
        caches.match(e.request).then(function (response) {
            return response || fetch(e.request);
        })
    );
});

/* Delete old caches */
self.addEventListener('activate', function (e) {
    e.waitUntil(
        caches.keys().then(function (keyList) {
            return Promise.all(keyList.map(function (key) {
                if (key !== cacheName) {
                    return caches.delete(key);
                }
            }));
        })
    );
    return self.clients.claim();
});
