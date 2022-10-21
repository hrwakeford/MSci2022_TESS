import os
import pickle

import astropy
import lightkurve as lk
from astropy.utils.masked import Masked

print("started")

# Config.
TIC = 'TIC 66818296' #WASP-17 / TIC 66818296
repo_path = 'C:\\Users\\Student\\OneDrive\\MSci project\\MSci2022_TESS\\'
LOAD_FROM_CACHE = True


# Retrieve data.
cache_dir = os.path.join(repo_path, 'lc_cache', '{}.p'.format(TIC))
cache_pickle = os.path.join(cache_dir, '{}.p'.format(TIC))
if LOAD_FROM_CACHE and os.path.exists(cache_pickle):
    # From cache.
    with open(cache_pickle, 'rb') as f:
        lc_collection = pickle.load(f)
else:
    # From MAST data archive.
    print("Searching")
    search_result = lk.search_lightcurve(
        target=TIC,
        mission='TESS', author='SPOC')
    print("trying to download")
    lc_collection = search_result.download_all()
    print("Search done")
    print(lc_collection)
    # Save to cache.
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    with open(cache_pickle, 'wb') as f:
        pickle.dump(lc_collection, f)

# Collate all sectors into one light curve.
lc = lc_collection.stitch(corrector_func=lambda x: x.remove_nans().normalize(unit='unscaled'))

print("Done")


