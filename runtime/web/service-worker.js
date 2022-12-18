var cacheName = 'renpy-web-game';

/* Start the service worker and cache all of the app's content or use the existing one */
self.addEventListener('install', function (e) {
    console.log('Service worker installed.');
    self.skipWaiting();
});

self.addEventListener('activate', function (e) {
    return self.clients.claim();
});

/**
 * Serves the cached version of the request if it exists, otherwise fetches the
 * request from the network and caches it. Fetch is used in the default mode,
 * which will use the cache for most network requests, freshening the cache
 * as required.
 */
async function fetchAndCache(request) {
    const cache = await caches.open(cacheName);

    try {
        const response = await fetch(request);
        await cache.put(request, response.clone());
        return response;
    } catch (e) {
        try {
            const response = await cache.match(request);
            if (response) {
                console.log('Served from cache: ' + request.url);
                return response;
            }
        } catch (e) {
            // pass
        }

        console.log('Not found in cache: ' + request.url);

        throw e;
    }
}


/* Serve cached content when offline */
self.addEventListener('fetch', function (e) {
    e.respondWith(fetchAndCache(e.request));
});

self.addEventListener('message', function (e) {
    if (e.data == "clearCache") {
        caches.delete(cacheName);
        console.log("Cache cleared in service worker.");
    }
});
