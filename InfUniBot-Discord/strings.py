from config import *

help_string = """\n.corsi -> lista completa dei link ai canali telegram di tutti i corsi \n
                 \n.s1 -> lista completa dei link ai canali telegram dei corsi del primo semestre \n
                 \n.s2 -> lista completa dei link ai canali telegram dei corsi del secondo semestre \n
                 \n.social -> lista completa dei link ai canali social della nostra classe\n
                 \n.appunti -> lista di link con appunti vari ed eventuali\n
                 \n.unisa -> lista di link utili dell'unisa\n
                 \n.info -> vabbè oh c'è bisogno di spiegare pure questo?\n """

courses_string = string_array['ADE'] + string_array['PR1'] + string_array['MD'] + string_array['OFA'] + string_array['PSD'] + string_array['MMI'] + string_array['ANAL'] 

first_year_first_semester_string = string_array['ADE'] + string_array['PR1'] + string_array['MD'] + string_array['OFA']

first_year_second_semester_string = string_array['PSD'] + string_array['MMI'] + string_array['ANAL']

first_year_string = first_year_first_semester_string + first_year_second_semester_string

second_year_first_semester_string = string_array['BD'] + string_array['POO'] + string_array['SO']

second_year_second_semester_string = string_array['PA'] + string_array['CPM'] + string_array['RETI'] + string_array['TSW']

second_year_string = second_year_first_semester_string + second_year_second_semester_string

social_string = string_array['whatsapp'] + string_array['telegram'] + string_array['discord']

note_string = string_array['hubmd'] + string_array['nicotera'] 

unisa_string = string_array['elearning'] + string_array['unisa'] + string_array['moodle'] + string_array['esse3']

