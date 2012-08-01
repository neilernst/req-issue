CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    email TEXT,
    firstname TEXT,
    lastname TEXT,
    issuetrk_id TEXT,
    repo_id TEXT,
    role_type TEXT -- may be PMC, committer, contrib, user etc.
);

CREATE table work_item (
    id INTEGER primary key,
    name TEXT, -- the title of the work item
    summary TEXT, -- absract
    tool_id TEXT, -- e.g. LUCENE-1458
    url TEXT,
    created,
    creator INTEGER, -- from the user table
    closed,
    issue_type,
    fix_version
);

CREATE table work_item_rel (
    id INTEGER primary key,
    from_item INTEGER,
    to_item INTEGER
); -- dependencies in wokr items

CREATE table comment (
    id INTEGER primary key,
    date TEXT,
    user_id INTEGER,
    issue_id INTEGER,
    content TEXT
);
-- what about status of the item, e.g. modifications to closed/open, release target, milestone, etc.

-- CREATE table changeset (
--     id INTEGER primary key,
--     date TEXT,
--     commit_msg TEXT,
--     revision TEXT,
--     sha1 TEXT,
--     committer TEXT -- just use the SCM committer name
-- );

-- if you are using cvsanaly to extract the SCM data, just create this view instead.
-- CREATE VIEW changeset as
-- select s.rev,  s.date, s.message, p.name from
-- scmlog as s, people as p
-- where s.committer_id = p.id;

CREATE table file (
    id INTEGER PRIMARY KEY,
    path TEXT,
    changed TEXT,
    CREATEd TEXT
);

CREATE table file_changeset (
    id INTEGER PRIMARY KEY,
    changeset_id INTEGER,
    file_id INTEGER
); -- map a file to one or more changesets

 -- later
-- CREATE TABLE email (id INTEGER PRIMARY KEY, subject, date, sender);
-- CREATE table website ();
-- CREATE TABLE sources ();
-- CREATE table tests ();
-- CREATE table nfr_keywords (id, term) as (1,maintainability, 2, portability) -- essentially the wordbag from MSR

-- queries that DEFINE the feature
-- Just anything that is selected from the initial choice of the work item. So select the right issue number, then add in the

-- queries which look for related features
