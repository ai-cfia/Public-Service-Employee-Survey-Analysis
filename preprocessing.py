import pandas as pd

# fetch the survey results of 2018 for Public Service and CFIA

data_2018 = data[(data["SURVEYR"] == 2018) & (data["BYCOND"].isnull())]
data_2018_ps = data_2018[data_2018["LEVEL1ID"] == 0]
data_2018_cfia = data_2018[data_2018["LEVEL1ID"] == 86]

# My Job

data_2018_ps_myjob = data_2018_ps[(data_2018_ps["QUESTION"] == "Q01") |
        (data_2018_ps["QUESTION"] == "Q02") |
        (data_2018_ps["QUESTION"] == "Q03") |
        (data_2018_ps["QUESTION"] == "Q04") |
        (data_2018_ps["QUESTION"] == "Q05") |
        (data_2018_ps["QUESTION"] == "Q06") |
        (data_2018_ps["QUESTION"] == "Q07") |
        (data_2018_ps["QUESTION"] == "Q08") |
        (data_2018_ps["QUESTION"] == "Q09") |
        (data_2018_ps["QUESTION"] == "Q10") |
        (data_2018_ps["QUESTION"] == "Q11") |
        (data_2018_ps["QUESTION"] == "Q12") |
        (data_2018_ps["QUESTION"] == "Q13") |
        (data_2018_ps["QUESTION"] == "Q14") |
        (data_2018_ps["QUESTION"] == "Q15") |
        (data_2018_ps["QUESTION"] == "Q16a") |
        (data_2018_ps["QUESTION"] == "Q16b") |
        (data_2018_ps["QUESTION"] == "Q16c") |
        (data_2018_ps["QUESTION"] == "Q16d") |
        (data_2018_ps["QUESTION"] == "Q16e") |
        (data_2018_ps["QUESTION"] == "Q16f") |
        (data_2018_ps["QUESTION"] == "Q16g")]

data_2018_cfia_myjob = data_2018_cfia[(data_2018_cfia["QUESTION"] == "Q01") |
        (data_2018_cfia["QUESTION"] == "Q02") |
        (data_2018_cfia["QUESTION"] == "Q03") |
        (data_2018_cfia["QUESTION"] == "Q04") |
        (data_2018_cfia["QUESTION"] == "Q05") |
        (data_2018_cfia["QUESTION"] == "Q06") |
        (data_2018_cfia["QUESTION"] == "Q07") |
        (data_2018_cfia["QUESTION"] == "Q08") |
        (data_2018_cfia["QUESTION"] == "Q09") |
        (data_2018_cfia["QUESTION"] == "Q10") |
        (data_2018_cfia["QUESTION"] == "Q11") |
        (data_2018_cfia["QUESTION"] == "Q12") |
        (data_2018_cfia["QUESTION"] == "Q13") |
        (data_2018_cfia["QUESTION"] == "Q14") |
        (data_2018_cfia["QUESTION"] == "Q15") |
        (data_2018_cfia["QUESTION"] == "Q16a") |
        (data_2018_cfia["QUESTION"] == "Q16b") |
        (data_2018_cfia["QUESTION"] == "Q16c") |
        (data_2018_cfia["QUESTION"] == "Q16d") |
        (data_2018_cfia["QUESTION"] == "Q16e") |
        (data_2018_cfia["QUESTION"] == "Q16f") |
        (data_2018_cfia["QUESTION"] == "Q16g")]

# My Work unit

data_2018_ps_myworkunit = data_2018_ps[(data_2018_ps["QUESTION"] == "Q17") |
        (data_2018_ps["QUESTION"] == "Q18") |
        (data_2018_ps["QUESTION"] == "Q19") |
        (data_2018_ps["QUESTION"] == "Q20") |
        (data_2018_ps["QUESTION"] == "Q21")]

data_2018_cfia_myworkunit = data_2018_cfia[(data_2018_cfia["QUESTION"] == "Q17") |
        (data_2018_cfia["QUESTION"] == "Q18") |
        (data_2018_cfia["QUESTION"] == "Q19") |
        (data_2018_cfia["QUESTION"] == "Q20") |
        (data_2018_cfia["QUESTION"] == "Q21")]

# My Immediate Supervisor

data_2018_ps_myimmediatesupervisor = data_2018_ps[(data_2018_ps["QUESTION"] == "Q22") |
        (data_2018_ps["QUESTION"] == "Q23") |
        (data_2018_ps["QUESTION"] == "Q24") |
        (data_2018_ps["QUESTION"] == "Q25") |
        (data_2018_ps["QUESTION"] == "Q26")]

data_2018_cfia_myimmediatesupervisor = data_2018_cfia[(data_2018_cfia["QUESTION"] == "Q22") |
        (data_2018_cfia["QUESTION"] == "Q23") |
        (data_2018_cfia["QUESTION"] == "Q24") |
        (data_2018_cfia["QUESTION"] == "Q25") |
        (data_2018_cfia["QUESTION"] == "Q26")]

# Senior Management

data_2018_ps_seniormanagement = data_2018_ps[(data_2018_ps["QUESTION"] == "Q28") |
        (data_2018_ps["QUESTION"] == "Q29") |
        (data_2018_ps["QUESTION"] == "Q30") |
        (data_2018_ps["QUESTION"] == "Q31") |
        (data_2018_ps["QUESTION"] == "Q32")]

data_2018_cfia_seniormanagement = data_2018_cfia[(data_2018_cfia["QUESTION"] == "Q28") |
        (data_2018_cfia["QUESTION"] == "Q29") |
        (data_2018_cfia["QUESTION"] == "Q30") |
        (data_2018_cfia["QUESTION"] == "Q31") |
        (data_2018_cfia["QUESTION"] == "Q32")]

# My Organization

data_2018_ps_myorganization = data_2018_ps[(data_2018_ps["QUESTION"] == "Q33") |
        (data_2018_ps["QUESTION"] == "Q34") |
        (data_2018_ps["QUESTION"] == "Q35") |
        (data_2018_ps["QUESTION"] == "Q36") |
        (data_2018_ps["QUESTION"] == "Q37") |
        (data_2018_ps["QUESTION"] == "Q38") |
        (data_2018_ps["QUESTION"] == "Q39") |
        (data_2018_ps["QUESTION"] == "Q40") |
        (data_2018_ps["QUESTION"] == "Q41") |
        (data_2018_ps["QUESTION"] == "Q42") |
        (data_2018_ps["QUESTION"] == "Q43") |
        (data_2018_ps["QUESTION"] == "Q44") |
        (data_2018_ps["QUESTION"] == "Q45")]

data_2018_cfia_myorganization = data_2018_cfia[(data_2018_cfia["QUESTION"] == "Q33") |
        (data_2018_cfia["QUESTION"] == "Q34") |
        (data_2018_cfia["QUESTION"] == "Q35") |
        (data_2018_cfia["QUESTION"] == "Q36") |
        (data_2018_cfia["QUESTION"] == "Q37") |
        (data_2018_cfia["QUESTION"] == "Q38") |
        (data_2018_cfia["QUESTION"] == "Q39") |
        (data_2018_cfia["QUESTION"] == "Q40") |
        (data_2018_cfia["QUESTION"] == "Q41") |
        (data_2018_cfia["QUESTION"] == "Q42") |
        (data_2018_cfia["QUESTION"] == "Q43") |
        (data_2018_cfia["QUESTION"] == "Q44") |
        (data_2018_cfia["QUESTION"] == "Q45")]

# Stress and Well-Being

data_2018_ps_stressandwellbeing = data_2018_ps[(data_2018_ps["QUESTION"] == "Q62a") |
        (data_2018_ps["QUESTION"] == "Q62b") |
        (data_2018_ps["QUESTION"] == "Q62c") |
        (data_2018_ps["QUESTION"] == "Q62d") |
        (data_2018_ps["QUESTION"] == "Q62e") |
        (data_2018_ps["QUESTION"] == "Q62f") |
        (data_2018_ps["QUESTION"] == "Q62g") |
        (data_2018_ps["QUESTION"] == "Q62h") |
        (data_2018_ps["QUESTION"] == "Q62i") |
        (data_2018_ps["QUESTION"] == "Q62j") |
        (data_2018_ps["QUESTION"] == "Q62k") |
        (data_2018_ps["QUESTION"] == "Q62l") |
        (data_2018_ps["QUESTION"] == "Q62m") |
        (data_2018_ps["QUESTION"] == "Q62n") |
        (data_2018_ps["QUESTION"] == "Q62o") |
        (data_2018_ps["QUESTION"] == "Q62p") |
        (data_2018_ps["QUESTION"] == "Q62q") |
        (data_2018_ps["QUESTION"] == "Q62r") |
        (data_2018_ps["QUESTION"] == "Q62s") |
        (data_2018_ps["QUESTION"] == "Q63") |
        (data_2018_ps["QUESTION"] == "Q64") |
        (data_2018_ps["QUESTION"] == "Q65") |
        (data_2018_ps["QUESTION"] == "Q66")]

data_2018_cfia_stressandwellbeing = data_2018_cfia[(data_2018_cfia["QUESTION"] == "Q62a") |
        (data_2018_cfia["QUESTION"] == "Q62b") |
        (data_2018_cfia["QUESTION"] == "Q62c") |
        (data_2018_cfia["QUESTION"] == "Q62d") |
        (data_2018_cfia["QUESTION"] == "Q62e") |
        (data_2018_cfia["QUESTION"] == "Q62f") |
        (data_2018_cfia["QUESTION"] == "Q62g") |
        (data_2018_cfia["QUESTION"] == "Q62h") |
        (data_2018_cfia["QUESTION"] == "Q62i") |
        (data_2018_cfia["QUESTION"] == "Q62j") |
        (data_2018_cfia["QUESTION"] == "Q62k") |
        (data_2018_cfia["QUESTION"] == "Q62l") |
        (data_2018_cfia["QUESTION"] == "Q62m") |
        (data_2018_cfia["QUESTION"] == "Q62n") |
        (data_2018_cfia["QUESTION"] == "Q62o") |
        (data_2018_cfia["QUESTION"] == "Q62p") |
        (data_2018_cfia["QUESTION"] == "Q62q") |
        (data_2018_cfia["QUESTION"] == "Q62r") |
        (data_2018_cfia["QUESTION"] == "Q62s") |
        (data_2018_cfia["QUESTION"] == "Q63") |
        (data_2018_cfia["QUESTION"] == "Q64") |
        (data_2018_cfia["QUESTION"] == "Q65") |
        (data_2018_cfia["QUESTION"] == "Q66")]