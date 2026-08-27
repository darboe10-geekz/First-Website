--create
CREATE TABLE PROJECTS (
    project_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_name VARCHAR2(100) NOT NULL,
    start_date DATE DEFAULT SYSDATE
);

--insert in team geekz table
INSERT INTO TEAM_GEEKZ (TEAM_GEEKZ.MEMBER_NAME) 
VALUES ('Pops_Senior');
commit;

--insert in proeject table
INSERT INTO PROJECT (PROJECT.PROJECT_NAME) 
VALUES ('Database Development Project');
commit;


--select  
SELECT * FROM PROJECT;
SELECT * FROM TEAM_GEEKZ;

--delete
DELETE FROM project
WHERE project_id = 21;

--update
UPDATE team_geekz
SET team_geekz.PROJECT_ID = 21
WHERE team_geekz.PROJECT_ID =7;
COMMIT;

--Alter table --add column
ALTER TABLE TEAM_GEEKZ 
MODIFY STATUS VARCHAR2(50);

--Alter table --Rename column
ALTER TABLE PROEJECT
RENAME TO project;

--drop table
DROP TABLE ex;

--Basic join querry
SELECT 
    team_geekz.member_id,
    team_geekz.member_name,
    team_geekz.status,
    project.project_id,
    project.project_name,
    project.start_date
FROM
    project 
INNER join
    team_geekz  ON team_geekz.project_id = project.project_id
ORDER by
    team_geekz.MEMBER_ID;
commit;

--case statement
SELECT 
    team_geekz.member_id,
    team_geekz.member_name,
    team_geekz.status,
    CASE
        WHEN TEAM_GEEKZ.STATUS = 'Active' THEN 'Active'
        WHEN TEAM_GEEKZ.STATUS = 'Inactive' THEN 'Inactive'
        ELSE 'Pending'
    END AS MEMBER_STATUS
FROM
    team_geekz;
commit;

--case statement Counting numbers per segment
SELECT 
    CASE
        WHEN TEAM_GEEKZ.STATUS = 'Active' THEN 'Active'
        WHEN TEAM_GEEKZ.STATUS = 'Inactive' THEN 'Inactive'
        ELSE 'Pending'
    END AS MEMBER_STATUS,
    COUNT (*) AS Number_Status
FROM team_geekz
GROUP BY 
    CASE 
        WHEN TEAM_GEEKZ.STATUS = 'Active' THEN 'Active'
        WHEN TEAM_GEEKZ.STATUS = 'Inactive' THEN 'Inactive'
        ELSE 'Pending'
    END;
commit;
