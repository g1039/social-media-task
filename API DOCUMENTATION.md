API Documentation for Social Media Activity Endpoint
====================================================


Overview
--------

This API provides a single endpoint that fetches and returns the activity count from various social media platforms (Twitter, Facebook, and Instagram). It uses multithreading to fetch data concurrently from these platforms.

Base URL
--------

```
http://0.0.0.0:8080/

```

Endpoint
--------

GET /

Fetches the social media activity counts from Twitter, Facebook, and Instagram.

URL: /
Method: GET
Auth required: No
Permissions required: No

Request Parameters
------------------

This endpoint does not require any request parameters or body.

Response
--------

Content-Type: application/json
Status Code: 200 OK

Example Response:

```
{
    "twitter": 3,
    "facebook": 2,
    "instagram": 5
}
```

twitter: Number of activities from Twitter.
facebook: Number of activities from Facebook.
instagram: Number of activities from Instagram.

Error Handling
--------------

If there is an issue with fetching data from any of the platforms or processing the request, the API will return 0 for the affected platform(s).

Example Error Response:

```
{
    "twitter": 0,
    "facebook": 2,
    "instagram": 5
}
```