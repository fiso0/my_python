import cgi
# import cgitb; cgitb.enable()

import athletemodel
import yate


form_data=cgi.FieldStorage()
athlete_name=form_data['which_athlete'].value

all_athletes=athletemodel.get_from_store()
athlete=all_athletes[athlete_name]

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: "+athlete_name+", DOB: "+athlete.dob+"."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athlete.top3))
print(yate.include_footer({"Home":"/index.html","Select another athlete":"generate_list.py"}))