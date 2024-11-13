# Definerer konstantene først
km_per_ar = 10000
forsikring_el = 5000
forsikring_bensin = 7500
trafikkforsikringsavgift_pr_dag = 8.38
stromforbruk_el_pr_km = 0.2
strompris_per_kwh = 2.00
besnin_pr_km = 1.0
bom_el_pr_km = 0.1
bom_bensin_pr_km = 0.3

# regner ut årlig trafikkforsikringsavgift
forsikring_aarlig = trafikkforsikringsavgift_pr_dag * 365

# Regner ut årlig kostnad for elbil
arlig_kostnad_el = (
    forsikring_el +
    forsikring_aarlig +
    (stromforbruk_el_pr_km * strompris_per_kwh * km_per_ar) +
    (bom_el_pr_km * km_per_ar)
)

# regner ut årlig kostnad for bensinbil
arlig_kostnad_bensin = (
    forsikring_bensin +
    forsikring_aarlig +
    (besnin_pr_km * km_per_ar) +
    (bom_bensin_pr_km * km_per_ar)
)

# Regner ut differanse
aarlig_kostnad_forskjell = arlig_kostnad_bensin - arlig_kostnad_el

# Skriver ut resultat
print(f"Årlige totalkostnader for elbil: {arlig_kostnad_el:.2f} kr")
print(f"Årlige totalkostnader for bensinbil: {arlig_kostnad_bensin:.2f} kr")
print(f"Årlig kostnadsdifferanse: {aarlig_kostnad_forskjell:.2f} kr")
