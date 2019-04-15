import matplotlib.pyplot as plt
import numpy as np

# My Jobs - Positive vs Negative

stat_ps_myjob = data_2018_ps_myjob.mean(axis = 0)[15: 18]
stat_cfia_myjob = data_2018_cfia_myjob.mean(axis = 0)[15: 18]

df_ps_myjob = pd.DataFrame({
        "Level": "PS",
        "Entry": stat_ps_myjob.index,
        "Stats": stat_ps_myjob.values
        })
df_cfia_myjob = pd.DataFrame({
        "Level": "CFIA",
        "Entry": stat_cfia_myjob.index,
        "Stats": stat_cfia_myjob.values
        })
df_myjob = pd.concat([df_ps_myjob, df_cfia_myjob])

cols = ["PS", "CFIA"]
vals = df_ps_myjob["Entry"].values
pivot_myjob = pd.pivot_table(df_myjob,
                             index = "Entry",
                             columns = "Level",
                             values = "Stats").reindex(columns = cols, index = vals)

fig_myjob = plt.figure(figsize=(8, 6))
ax_myjob = fig_myjob.add_subplot(111)
pivot_myjob.plot(kind = "bar", ax = ax_myjob)
ax_myjob.set_xlabel("")
ax_myjob.set_ylabel("Percentage")
ax_myjob.set_title("My Job")
fig_myjob.savefig("diagrams/myjob.png")

# My Work Unit - Positive vs Negative

stat_ps_myworkunit = data_2018_ps_myworkunit.mean(axis = 0)[15: 18]
stat_cfia_myworkunit = data_2018_cfia_myworkunit.mean(axis = 0)[15: 18]

df_ps_myworkunit = pd.DataFrame({
        "Level": "PS",
        "Entry": stat_ps_myworkunit.index,
        "Stats": stat_ps_myworkunit.values
        })
df_cfia_myworkunit = pd.DataFrame({
        "Level": "CFIA",
        "Entry": stat_cfia_myworkunit.index,
        "Stats": stat_cfia_myworkunit.values
        })
df_myworkunit = pd.concat([df_ps_myworkunit, df_cfia_myworkunit])

cols = ["PS", "CFIA"]
vals = df_ps_myworkunit["Entry"].values
pivot_myworkunit = pd.pivot_table(df_myworkunit,
                                  index = "Entry",
                                  columns = "Level",
                                  values = "Stats").reindex(columns = cols, index = vals)

fig_myworkunit = plt.figure(figsize=(8, 6))
ax_myworkunit = fig_myworkunit.add_subplot(111)
pivot_myworkunit.plot(kind = "bar", ax = ax_myworkunit)
ax_myworkunit.set_xlabel("")
ax_myworkunit.set_ylabel("Percentage")
ax_myworkunit.set_title("My Work Unit")
fig_myworkunit.savefig("diagrams/myworkunit.png")

# My Immediate Supervisor - Positive vs Negative

stat_ps_myimmediatesupervisor = data_2018_ps_myimmediatesupervisor.mean(axis = 0)[15: 18]
stat_cfia_myimmediatesupervisor = data_2018_cfia_myimmediatesupervisor.mean(axis = 0)[15: 18]

df_ps_myimmediatesupervisor = pd.DataFrame({
        "Level": "PS",
        "Entry": stat_ps_myimmediatesupervisor.index,
        "Stats": stat_ps_myimmediatesupervisor.values
        })
df_cfia_myimmediatesupervisor = pd.DataFrame({
        "Level": "CFIA",
        "Entry": stat_cfia_myimmediatesupervisor.index,
        "Stats": stat_cfia_myimmediatesupervisor.values
        })
df_myimmediatesupervisor = pd.concat([df_ps_myimmediatesupervisor, df_cfia_myimmediatesupervisor])

cols = ["PS", "CFIA"]
vals = df_ps_myimmediatesupervisor["Entry"].values
pivot_myimmediatesupervisor = pd.pivot_table(df_myimmediatesupervisor,
                                             index = "Entry",
                                             columns = "Level",
                                             values = "Stats").reindex(columns = cols, index = vals)

fig_myimmediatesupervisor = plt.figure(figsize=(8, 6))
ax_myimmediatesupervisor = fig_myimmediatesupervisor.add_subplot(111)
pivot_myimmediatesupervisor.plot(kind = "bar", ax = ax_myimmediatesupervisor)
ax_myimmediatesupervisor.set_xlabel("")
ax_myimmediatesupervisor.set_ylabel("Percentage")
ax_myimmediatesupervisor.set_title("My Immediate Supervisor")
fig_myimmediatesupervisor.savefig("diagrams/myimmediatesupervisor.png")

# Senior Management - Positive vs Negative

stat_ps_seniormanagement = data_2018_ps_seniormanagement.mean(axis = 0)[15: 18]
stat_cfia_seniormanagement = data_2018_cfia_seniormanagement.mean(axis = 0)[15: 18]

df_ps_seniormanagement = pd.DataFrame({
        "Level": "PS",
        "Entry": stat_ps_seniormanagement.index,
        "Stats": stat_ps_seniormanagement.values
        })
df_cfia_seniormanagement = pd.DataFrame({
        "Level": "CFIA",
        "Entry": stat_cfia_seniormanagement.index,
        "Stats": stat_cfia_seniormanagement.values
        })
df_seniormanagement = pd.concat([df_ps_seniormanagement, df_cfia_seniormanagement])

cols = ["PS", "CFIA"]
vals = df_ps_seniormanagement["Entry"].values
pivot_seniormanagement = pd.pivot_table(df_seniormanagement,
                                        index = "Entry",
                                        columns = "Level",
                                        values = "Stats").reindex(columns = cols, index = vals)

fig_seniormanagement = plt.figure(figsize=(8, 6))
ax_seniormanagement = fig_seniormanagement.add_subplot(111)
pivot_seniormanagement.plot(kind = "bar", ax = ax_seniormanagement)
ax_seniormanagement.set_xlabel("")
ax_seniormanagement.set_ylabel("Percentage")
ax_seniormanagement.set_title("Senior Management")
fig_seniormanagement.savefig("diagrams/seniormanagement.png")

# My Organization - Positive vs Negative

stat_ps_myorganization = data_2018_ps_myorganization.mean(axis = 0)[15: 18]
stat_cfia_myorganization = data_2018_cfia_myorganization.mean(axis = 0)[15: 18]

df_ps_myorganization = pd.DataFrame({
        "Level": "PS",
        "Entry": stat_ps_myorganization.index,
        "Stats": stat_ps_myorganization.values
        })
df_cfia_myorganization = pd.DataFrame({
        "Level": "CFIA",
        "Entry": stat_cfia_myorganization.index,
        "Stats": stat_cfia_myorganization.values
        })
df_myorganization = pd.concat([df_ps_myorganization, df_cfia_myorganization])

cols = ["PS", "CFIA"]
vals = df_ps_myorganization["Entry"].values
pivot_myorganization = pd.pivot_table(df_myorganization,
                                      index = "Entry",
                                      columns = "Level",
                                      values = "Stats").reindex(columns = cols, index = vals)

fig_myorganization = plt.figure(figsize=(8, 6))
ax_myorganization = fig_myorganization.add_subplot(111)
pivot_myorganization.plot(kind = "bar", ax = ax_myorganization)
ax_myorganization.set_xlabel("")
ax_myorganization.set_ylabel("Percentage")
ax_myorganization.set_title("My Organization")
fig_myorganization.savefig("diagrams/myorganization.png")

# Stress and Well-Being - Positive vs Negative

stat_ps_stressandwellbeing = data_2018_ps_stressandwellbeing.mean(axis = 0)[15: 18]
stat_cfia_stressandwellbeing = data_2018_cfia_stressandwellbeing.mean(axis = 0)[15: 18]

df_ps_stressandwellbeing = pd.DataFrame({
        "Level": "PS",
        "Entry": stat_ps_stressandwellbeing.index,
        "Stats": stat_ps_stressandwellbeing.values
        })
df_cfia_stressandwellbeing = pd.DataFrame({
        "Level": "CFIA",
        "Entry": stat_cfia_stressandwellbeing.index,
        "Stats": stat_cfia_stressandwellbeing.values
        })
df_stressandwellbeing = pd.concat([df_ps_stressandwellbeing, df_cfia_stressandwellbeing])

cols = ["PS", "CFIA"]
vals = df_ps_stressandwellbeing["Entry"].values
pivot_stressandwellbeing = pd.pivot_table(df_stressandwellbeing,
                                          index = "Entry",
                                          columns = "Level",
                                          values = "Stats").reindex(columns = cols, index = vals)

fig_stressandwellbeing = plt.figure(figsize=(8, 6))
ax_stressandwellbeing = fig_stressandwellbeing.add_subplot(111)
pivot_stressandwellbeing.plot(kind = "bar", ax = ax_stressandwellbeing)
ax_stressandwellbeing.set_xlabel("")
ax_stressandwellbeing.set_ylabel("Percentage")
ax_stressandwellbeing.set_title("Stress and Well-Being")
fig_stressandwellbeing.savefig("diagrams/stressandwellbeing.png")