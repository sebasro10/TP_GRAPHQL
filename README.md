# TP GRAPHQL

**Author**: Sebastian Romero <sebastian.romero@imt-atlantique.net>

This repository has a folder for each microservice:

* `/booking`
* `/movie`
* `/showtime`
* `/user`

In the `docker-compose.yml` file you can see the information about the services and their exposed ports.

## What was made of the TP?

In this repository from commits you can clearly see the progress of the TP:

* Commit [tutorial](https://github.com/sebasro10/TP_GRAPHQL/commit/57a8967b574158404bf87a8146299316819013eb)
* Commit [code of TP_GRPC](https://github.com/sebasro10/TP_GRAPHQL/commit/0a6c6fe63705fe61f458cd15b6766810ea9fc0bf)
* Commit [TP vert](https://github.com/sebasro10/TP_GRAPHQL/commit/9f4654ff904e833ddcda37f36c7b4a9dd78926d9)

## Run project

Build or rebuild services
```bash
docker-compose build
```

Create and start containers
```bash
docker-compose up
```

Stop and remove containers, networks
```bash
docker-compose down
```

## Tests GRAPHQL

To test the `movie` service directly you can use the following requests from the playground GraphQL (http://localhost:3001/graphql) 
or from postman:

```bash
query{
  movie_with_id(_id:"39ab85e5-5e8e-4dc5-afea-65dc368bd7ab") {
    title
    director
    rating
    actors{
      firstname
      lastname
      birthyear
    }
  }
}
```

```bash
query{
  actor_with_id(_id:"actor1") {
    firstname
    lastname
    birthyear
  }
}
```

```bash
query{
  get_list_movies {
    title
    director
    rating
  }
}
```

```bash
query{
  movie_with_title(_title:"Spectre") {
    title
    director
    rating
  }
}
```

```bash
query{
  movies_by_director(_director:"Sam Mendes") {
    title
    director
    rating
    actors{
      firstname
      lastname
      birthyear
    }
  }
}
```

```bash
mutation{
    update_movie_rate(_id:"a8034f44-aee4-44cf-b32c-74cf452aaaae",_rate:8.8) {
        title
        rating
    }
}
```

```bash
mutation{
    create_movie(_movie:{id:"newId",title:"newTitle",director:"newDirector",rating:8.6}) {
        message
    }
}
```

```bash
mutation{
    delete_movie(_id:"newId") {
        title
        director
        rating
    }
}
```

## Tests from Postman

And you can test the `user` service from Postman by following the steps below:

* In Postman click on "Import" -> "Upload Files"
* Select the file with the contract (`user/UE-archi-distribuees-User-1.0.0-resolved.yaml`)
* Select the option "Generate collection from imported APIs" and in "Link this collection as" select "Test suite"
* Click on "Import"

Now, a collection has been created and you can test the methods.
