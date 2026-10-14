def calculate_ideal_gas(P=None, V=None, n=None, T=None):
  """
  Calculates the missing variables in PV=nRT.
  Pressure(P) in atm, Volume(V) in Litres,
  Moles(n) in mol, Temperature(T) in Kelvin.
  """
  R=0.08206 #Ideal gas constant in L*atm/(mol*K)
# Check which variable is missing and solve for it
if P is None:
    P = (n*r*t)/V
    return f"Pressure(P) =  {P:.4f} atm "
elif V is  None:
    V= (n*R*T)/P
    return f"Volume(V)= {V;.4f}L"
elif n is None:
    n = (P*V)/(R*T)
    return f"Amount(n)={n:.4f} mol"
elif T is None:
    T= (P*V)/(n*R)
    return f"Temperature(T) = {T:.2f} K"
else:
    return "All variables are already provided"
  #Example : Find the volume of 1 mol of gas at STP (1atm, 273.15K) 

print(calcualate_ideal_gas(P=1.0,n=1.0,T=273.15)
