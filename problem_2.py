import problem_1 as PONE

Prob = 0.4

Total_Times = 1000

N_time_steps = 20


myChort = PONE.Cohort(id=1, total_times=Total_Times, prob=Prob)
myChort.simlate(N_time_steps)

print(myChort.get_ave_game_time())
