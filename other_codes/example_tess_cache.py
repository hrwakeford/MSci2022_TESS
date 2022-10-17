#David Grant's cache code

import os
import pickle
import lightkurve as lk


# Config.
TIC = 'TIC 66818296'
repo_path = 'path/to/code'
LOAD_FROM_CACHE = True


# Retrieve data.
cache_dir = os.path.join(repo_path, '_cache', '{}.p'.format(TIC))
cache_pickle = os.path.join(cache_dir, '{}.p'.format(TIC))
if LOAD_FROM_CACHE and os.path.exists(cache_pickle):
    # From cache.
    with open(cache_pickle, 'rb') as f:
        lc_collection = pickle.load(f)
else:
    # From MAST data archive.
    search_result = lk.search_lightcurve(
        target=TIC,
        mission='TESS', author='SPOC',
        sector=None, exptime=None)
    lc_collection = search_result.download_all()

    # Save to cache.
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    with open(cache_pickle, 'wb') as f:
        pickle.dump(lc_collection, f)

# Collate all sectors into one light curve.
lc = lc_collection.stitch(corrector_func=lambda x: x.
                          remove_nans().normalize(unit='unscaled'))
