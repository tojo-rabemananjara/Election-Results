import numpy as np
import matplotlib.pyplot as plt

#surveying a subset of population of 10000 people - assuming all of them will vote
survey_responses = np.array(['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos'])


#total # who vote ceballos prediction
total_ceballos = len(survey_responses[survey_responses == 'Ceballos'])
print(total_ceballos)

#percent votes for ceballos prediction 47% 33/70
percentage_ceballos = np.mean(survey_responses == 'Ceballos')
print(percentage_ceballos)

#display histogram of binomial sample distribution for actual 54% outcome, numserveys (small num) and size = 10000 = population
#using the total number of survey, the sactual success rate (54%), and the total size of the town's population 10000
N=len(survey_responses)
P=.54
S=10000
possible_surveys = np.random.binomial(N, P, S) / float(N)
plt.hist(possible_surveys, range=(0,1), bins=30)
#calculate the % of surveys that could have an outcome of Ceballos receiving less than 50% of the vote
ceballos_loss_surveys = np.mean(possible_surveys < .5)
print(ceballos_loss_surveys)

#hypothetically increase the number of surveys from 33 out of 10000 to 700 out of 10000
N=700
large_survey = np.random.binomial(N, P, S) / float(N)

#display histogram of binomial sample distribution for actual 54% outcome, new larger hypothetical number of surveys, and size = 10000 = population
plt.hist(large_survey, range=(0,1), bins=30, alpha=0.4)

labels = ['70 surveys', '700 surveys']
plt.legend(labels)
plt.title('Sample Binomial Distribution for Votes for Cabellos')
plt.xlabel("Proportion of votes for Cabellos")
plt.ylabel("Votes for Cabellos (left half) & Kerrigan (right half)")
plt.show()

#probability that ceballos loses based on binomial model using produced with 700 surveys instead of 33
ceballos_loss_new = np.mean(large_survey < .5)
print(ceballos_loss_new)