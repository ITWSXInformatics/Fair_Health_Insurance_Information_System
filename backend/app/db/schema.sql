drop table if exists plaintexts;
create table example_table (
    id integer primary key autoincrement,
    name varchar not null,
    description varchar not null,
    -- path to the original plaintext
    p_path varchar not null,
    -- path to the scrubbed plaintext
    s_path varchar not null,
    -- path to the tokenized plaintext 
    t_path varchar not null,
    occ_path varchar not null

);
