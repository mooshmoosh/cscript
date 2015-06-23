#!/usr/bin/cscript --compiler-arguments="-lcurl"
#include <curl/curl.h>

CURL *curl;
CURLcode res;

curl = curl_easy_init();
if(!curl) {
    printf("Could not initialise curl\n");
    return 1;
}

curl_easy_setopt(curl, CURLOPT_URL, "http://example.com");
curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
res = curl_easy_perform(curl);
if(res != CURLE_OK)
  fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));

curl_easy_cleanup(curl);

