DROP TABLE IF EXISTS movies CASCADE;
DROP TABLE IF EXISTS movie_rate CASCADE;
DROP TABLE IF EXISTS streaming_disp CASCADE;
DROP TABLE IF EXISTS director CASCADE;
DROP TABLE IF EXISTS country CASCADE;
DROP TABLE IF EXISTS genero CASCADE;
DROP TABLE IF EXISTS clasificacion CASCADE;

CREATE TABLE director (
    director_ID SERIAL PRIMARY KEY,
    director_name character varying(250) NOT NULL
);

CREATE TABLE genero (
    genre_ID SERIAL PRIMARY KEY,
    genre_name character varying(250) NOT NULL
);

CREATE TABLE country (
    country_ID SERIAL PRIMARY KEY,
    country_name character varying(250) NOT NULL
);

CREATE TABLE clasificacion (
    clasificacion_ID SERIAL PRIMARY KEY,
    clasificacion_name character varying(250) NOT NULL
);

CREATE TABLE movies (
    movie_ID SERIAL PRIMARY KEY,
    movie_name character varying(250) NOT NULL,
    director_ID integer NOT NULL REFERENCES director(director_ID),
    genre_ID integer NOT NULL REFERENCES genero(genre_ID),
    budget FLOAT NOT NULL,
    revenue FLOAT NOT NULL,
    runtime integer NOT NULL,
    year integer NOT NULL,
    country_ID integer NOT NULL REFERENCES country(country_ID),
    clasificacion_ID integer NOT NULL REFERENCES clasificacion(clasificacion_ID)
);

CREATE TABLE movie_rate (
	rate_ID SERIAL PRIMARY KEY,
    movie_ID INT NOT NULL REFERENCES movies(movie_ID),
    imdb_rate FLOAT NOT NULL,
    tomatoe_rate FLOAT NOT NULL,
    imdb_votes FLOAT NOT NULL,
    imdb_votes_count integer NOT NULL,
    popularity FLOAT NOT NULL,
    movie_rate FLOAT NOT NULL
);

CREATE TABLE streaming_disp (
    streaming_ID SERIAL PRIMARY KEY,
    movie_ID INT NOT NULL REFERENCES movies(movie_ID),
    netflix integer NOT NULL,
    hulu integer NOT NULL,
    prime_video integer NOT NULL,
    disney integer NOT NULL
);
