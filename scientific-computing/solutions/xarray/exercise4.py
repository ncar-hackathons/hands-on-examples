# Computed climatology
sst_clim = ds_all.sst.groupby('time.month').mean(dim='time')

# Compute Anomaly
sst_anom = ds_all.sst.groupby('time.month') - sst_clim

# Compute ENSO index
sst_anom_nino34 = sst_anom.sel(lat=slice(-5, 5), lon=slice(190, 240))
print(sst_anom_nino34)

sst_anom_nino34_mean = sst_anom_nino34.mean(dim=('lon', 'lat'))
oni = sst_anom_nino34_mean.rolling(time=3).mean(dim='time')

# Plot the ENSO index 
fig, ax = plt.subplots();
sst_anom_nino34_mean.plot(ax=ax, label='raw');
oni.plot(ax=ax, label='smoothed');
ax.grid();

# create a categorical  dataarray
nino34 = xr.full_like(oni, 'none', dtype='U4')
nino34[oni >= 0.5] = 'nino'
nino34[oni <= -0.5] = 'nina'
print(nino34)


sst_nino_composite = sst_anom.groupby(nino34.rename('nino34')).mean(dim='time')
print(sst_nino_composite)

sst_nino_composite.plot(col='nino34');

