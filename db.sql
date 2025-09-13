create table categories(
id SERIAL PRIMARY KEY,
name VARCHAR(64) UNIQUE NOT NULL,
create_at TIMESTAMPTZ DEFAULT now()
);



