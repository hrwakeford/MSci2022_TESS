from astroquery.simbad import Simbad
result_table = Simbad.query_object("WASP-39b")
print(result_table)
print("")
for line in result_table[0]:
    print(line)
