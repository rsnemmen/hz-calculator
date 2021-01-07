#************************************************************************************
# This code calculates habitable zone 'fluxes' using the expression given in the 
# Kopparapu et al.(2014) paper. The corresponding output file is 'HZs.dat'. 
# It also generates a file 'HZ_coefficients.dat' that gives the coefficients for 
# the analytical expression.
#
# - Ravi kumar Kopparapu April 19 2014
# - Translated to python code by John Armstrong (jcarmstrong@weber.edu) 04 June 2014
# - Improved by Rodrigo Nemmen, Jan 6 2021
#
#***********************************************************************************
#************************************************************************************

import numpy as np

teff=input('Temperature (K): ')
lum=input('Luminosity (Lsun): ')
teff=float(teff)
lum=float(lum)

#************************************************************************************
# Coeffcients to be used in the analytical expression to calculate habitable zone flux 
# boundaries

seffsun  = np.array([1.776,1.107, 0.356, 0.320, 1.188, 0.99])
a = np.array([2.136e-4, 1.332e-4, 6.171e-5, 5.547e-5, 1.433e-4, 1.209e-4])
b = np.array([2.533e-8, 1.580e-8, 1.698e-9, 1.526e-9, 1.707e-8, 1.404e-8])
c = np.array([-1.332e-11, -8.308e-12, -3.198e-12, -2.874e-12, -8.968e-12, -7.418e-12])
d = np.array([-3.097e-15, -1.931e-15, -5.575e-16, -5.011e-16, -2.084e-15, -1.713e-15])
    
#********************************************************************
# Calculating HZ fluxes for stars with 2600 K < T_eff < 7200 K.
tstar = teff - 5780.0

seff = seffsun + a*tstar + b*tstar**2 + c*tstar**3 + d*tstar**4

starTemp=teff
recentVenus=seff[0]
runawayGreenhouse=seff[1]
maxGreenhouse=seff[2]
earlyMars=seff[3]
fivemeRunaway=seff[4]
tenthmeRunaway=seff[5]
    
# Conservative HZ. The abs was not originally here.
rin=np.sqrt(np.abs(lum/runawayGreenhouse))
rout=np.sqrt(np.abs(lum/maxGreenhouse))

# Optimistic HZ
rin_op=np.sqrt(np.abs(lum/recentVenus))
rout_op=np.sqrt(np.abs(lum/earlyMars))

print('Conservative habitable zone: '+str(round(rin,2))+'-'+str(round(rout,2))+' AU')
print('Optimistic habitable zone: '+str(round(rin_op,2))+'-'+str(round(rout_op,2))+' AU')

