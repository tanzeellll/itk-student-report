-- This is to get all student details who have not attemped any exercise

CREATE OR REPLACE VIEW student_report_exercise_na AS
SELECT u.id AS user_id, u.name, u.school, u.grade, u.division FROM `itk-dump`.users u
WHERE id NOT IN (SELECT DISTINCT(user_id) FROM `itk-dump`.student_report)
ORDER BY u.school, u.grade, u.division, u.name;
