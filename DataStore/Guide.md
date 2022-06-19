
# Data Store Guide
---

# About
> Data store is a data library, where anyone can save their data, in any format. Initially, we have handled only json format, but can also support xml etc.


```
{
    "data_format": "json",
    "data": [{
    }]
}

```

# Usage
> There are public apis exposed to users, where anyone can post their data using some endpoints that we have exposed.
> These are the operations and endpoints that are accessible to users

>The above json document is sample document and must be provided in record creation.

# */store/get*
### GET
> This endpoint get your record by providing it an id in query param

# */store/add*
### POST
> This endpoint creates a record by providing a data format mentioned above.

# */store/add-many*
### POST
> This endpoint creates a record by providing a data format mentioned above.


# */store/update*
### PATCH
> This endpoint updates a record by providing it an id in query param.

# */store/delete*
### DELETE
> This endpoint deletes a record by providing it an id in query param.

