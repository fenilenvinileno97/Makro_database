-- OBSERVATIONS

-- output table is correct but actual_code is uncorrectly assigned, each column entry should correspond to
-- MAX(local_code) GROUP BY 'local_code', and letter_code values should be there instead of actual_code


SELECT local_code, reagent_name, cas_number, chemical_category AS functional_group, location, observation, av_quantity, tot_quantity, size
FROM (SELECT local_code, code_to_category, reagent_name, cas_number, location, observation, av_quantity, tot_quantity, size
	FROM reagent_name AS r
		INNER JOIN code AS k ON r.id_local_code = k.id_local_code
		INNER JOIN container AS c ON c.id_reagent_name = r.id_reagent_name) AS x
	INNER JOIN chemical_category AS ch ON x.code_to_category = ch.actual_code;