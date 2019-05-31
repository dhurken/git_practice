def grade_converter(gpa):
  if gpa >= 4.0:
      grade = "A"
  elif gpa >= 3.0:
      grade = "B"
  elif gpa >= 2.0:
      grade = "C"
  elif gpa >= 1.0:
      grade = "D"
  elif gpa >= 0.0:
      ggrade = "F"
  return(grade)
  
ltrGrade = grade_converter(4.01)

print(ltrGrade)

#------------------------------------------

def applicant_selector(gpa,ps_score,ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
    return "This applicant should be given an in-person interview."
  else:
      return "This applicant should be rejected."

stuApp = applicant_selector(3.0,9,2.0)

print(stuApp)
