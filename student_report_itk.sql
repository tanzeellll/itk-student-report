USE `itk-dump`;

-- This is to get all student details, exercises & levels completed and to calculate school average
CREATE OR REPLACE VIEW student_report AS
SELECT uel.user_id, u.name AS name, u.school AS school, u.grade AS grade, u.division AS division, uel.exercise_id, uel.level, e.total_levels, uel.xml AS blocks, uel.status AS completion_status FROM user_exercise_levels uel
JOIN users u ON  uel.user_id = u.id
JOIN exercises e ON uel.exercise_id = e.id
ORDER BY u.school, u.grade, u.division, u.name, uel.level, uel.exercise_id;


-- Need to calculate School average & XML blocks used using a Python Script