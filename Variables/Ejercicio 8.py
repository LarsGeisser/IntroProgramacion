
# mi = monto inicial
mi  =  float ( input ( "¿Cuanto dinero estas invirtiendo?" ))
# ts = tasa de interes
ts  =  float ( input ( "¿Cual es la tasa de interes en donde vas a invertir?" ))
# pa = periodo de ahorro
pa  =  float ( input ( "¿Cuantos años vas a invertir?" ))
# mf = monto final (ganacia neta)
mf  =  mi * ( 1 + ts ) ** pa
print ( "la ganacia liquida es de:" , mf )